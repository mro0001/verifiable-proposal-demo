"""Count what A5 and Tables A10 and A11 report about the live judgment runs of October 8, 2026.

Purpose:
    Unpack the seven run folders of October 8 into a temporary folder and
    count, from their saved records alone, what the appendix reports about
    them. For every run that is the saved answers and retries, the items put to
    a model, and the warning and blocking findings. For a seeded run it is also
    the planted faults caught and the extra findings, from the run's own score,
    and how many of the faults that depend on judgment the model's own saved
    answers flag. For the seeded references run it is how many support verdicts
    differ from the recorded answers that come with the artifact, and how often
    the second model agreed. It also reruns, from the earlier copy, the trial
    of the earlier prose procedure with no model answers, a fixed record like
    the runs, and keeps its planted faults and those caught. Every number is
    one row of key and value, and a number the appendix writes as a word also
    gets a row with its word form.
Inputs:
    live_runs_2026-10-08.tar - the seven run folders of October 8, packed unchanged.
    artifact_public_f48459a.tar - git archive of the earlier public copy of the research artifact, for the truth files, recorded answers, and graphs of the procedures the runs used.
Outputs:
    live_runs.csv - the counts, one row per key.
    params_record_live.csv - the parameters this run read, written by the run.
Parameters:
    live_archive - the archive of the run folders.
    procedures_archive - the archive of the earlier copy of the research artifact, whose procedures the runs used.
    live_runs - each run as label=folder, the label naming the procedure (and graph version) and the test files.
    judgment_runs - the labels of the seeded runs whose judgment faults are read from the saved answers.
    differ_run - the label of the run whose support verdicts are compared with the recorded answers.
    support_step - the judgment step whose verdicts are compared.
    recheck_step - the second model's step.
    retry_suffix - the ending of a saved answer file that holds a retry.
    nojudge_stream - the earlier procedure run once more with no model answers at all.
    harness_programs - programs whose folders are left off the command path, so the trial finds no real harness.
    word_keys - result keys that also get a word form.
    word_cap_keys - result keys that also get a word form starting with a capital.
Assumptions:
    A run folder holds manifest.json, records/ with one record per step,
    responses/ with one folder per judgment step and one file per answer, and
    files/findings.json. A seeded run also holds score.json, written by the
    score command on October 8. A planted fault depends on judgment when the
    check its truth file names is a judgment step of the procedure's graph. A
    saved answer flags a problem when it gives a verdict other than supports,
    finds that documentation does not match its code, or finds a rationale
    dishonest or a change of meaning. An answer is read from the first opening
    brace to the last closing brace, and the retry is read when there is one.
    The truth files, recorded answers, and graphs are read from the earlier
    public copy of the artifact, commit f48459a, not as they stood on October 8.
    The runs used the earlier procedures, which the artifact's newest public
    copy, commit e22136c, no longer has, so that copy is not read here. The
    no-answer trial runs the earlier copy's procedure on its seeded test files
    from its verification_procedures folder, unpacked into the temporary
    folder, with a recorded answer file that holds no answers in place of each
    recorded answer file its test files come with, then scores the run. It
    runs with every home the workflow reads inside the temporary folder, with
    VG_OFFLINE set, with no bytecode written, and without the folders that hold
    a harness program on the command path.
"""
# step: Read parameters
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile

import yaml

import params_io
import results_io

P = params_io.Params(step="live", script="s2_live_runs.py")
FLAGGING = ("blocking", "warning")
HOMES = ("HOME", "AUDIT_HOME", "CONNECTIONS_HOME", "FEATURES_HOME", "XDG_CONFIG_HOME")


# step: Read answers
def pairs(text):
    """Split a parameter written as name=value words into (name, value) pairs, in order."""
    return [tuple(word.split("=", 1)) for word in text.split()]


def read_json(path):
    """Read one JSON file."""
    with open(path) as f:
        return json.load(f)


def parse_answer(text):
    """Return the answer object in a saved answer's text, or None when it does not parse."""
    try:
        return json.loads(text[text.index("{"):text.rindex("}") + 1])
    except ValueError:
        return None


def flags(answer):
    """True when a saved answer finds a problem with its item (see Assumptions)."""
    if not isinstance(answer, dict):
        return False
    if "verdict" in answer:
        return answer["verdict"] != "supports"
    if "matches" in answer:
        return answer["matches"] is False
    return answer.get("honest") is False or answer.get("meaning_changed") is True


def step_folder(run, step):
    """Return the run's responses folder for one judgment step, or None when the run has none."""
    folder = os.path.join(run, "responses")
    for name in sorted(os.listdir(folder)):
        if name.split("_", 1)[-1] == step:
            return os.path.join(folder, name)
    return None


def answer_of(run, step, item):
    """Return the parsed saved answer of one step for one item, its retry when there is one."""
    folder = step_folder(run, step)
    if folder is None:
        return None
    for name in (item + P["retry_suffix"], item + ".txt"):
        path = os.path.join(folder, name)
        if os.path.exists(path):
            with open(path) as f:
                return parse_answer(f.read())
    return None


def answered_items(run, step):
    """Return the items a step has a first saved answer for, retries left out."""
    folder = step_folder(run, step)
    if folder is None:
        return []
    return sorted(n[:-len(".txt")] for n in os.listdir(folder)
                  if n.endswith(".txt") and not n.endswith(P["retry_suffix"]))


# step: Planted faults
def judgment_faults(tf, stream):
    """Return the planted faults of a procedure's seeded test files whose check is a judgment step."""
    graph = yaml.safe_load(tf.extractfile("verification_procedures/graphs/" + stream + ".yaml"))
    judged = {n["id"] for n in graph["nodes"] if n.get("kind") == "judgment"}
    truth = yaml.safe_load(tf.extractfile("verification_procedures/fixtures/" + stream + "/seeded/truth.yaml"))
    return [f for f in truth["faults"] if f["check"] in judged]


# step: Count runs
def one_run(run, results, prefix):
    """Count one run's saved answers, judged items, and findings, and its score when it has one."""
    files = []
    for _, _, names in os.walk(os.path.join(run, "responses")):
        files.extend(names)
    results[prefix + "responses"] = len(files)
    results[prefix + "retries"] = sum(n.endswith(P["retry_suffix"]) for n in files)
    items = 0
    for name in sorted(os.listdir(os.path.join(run, "records"))):
        execution = read_json(os.path.join(run, "records", name)).get("execution") or {}
        if execution.get("type") == "judgment":
            items += execution.get("items", 0)
    results[prefix + "items"] = items
    findings = read_json(os.path.join(run, "files", "findings.json"))
    findings = findings["items"] if isinstance(findings, dict) else findings
    results[prefix + "findings"] = sum(f["severity"] in FLAGGING for f in findings)
    results[prefix + "graph_version"] = read_json(os.path.join(run, "manifest.json"))["graph"]["version"]
    score_file = os.path.join(run, "score.json")
    if os.path.exists(score_file):
        score = read_json(score_file)
        results[prefix + "faults"] = score["faults"]
        results[prefix + "caught"] = len(score["caught"])
        results[prefix + "extras"] = len(score["extra_findings"])


# step: No-answer trial
def child_env(base):
    """Return the environment the trial runs with (see Assumptions)."""
    env = dict(os.environ)
    for name in HOMES:
        env[name] = os.path.join(base, "homes", name.lower())
        os.makedirs(env[name], exist_ok=True)
    env["VG_OFFLINE"] = "1"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    harness = P["harness_programs"].split()
    # Drop each folder on the command path that holds a harness program.
    keep = [d for d in env.get("PATH", "").split(os.pathsep)
            if d and not any(os.path.exists(os.path.join(d, h)) for h in harness)]
    env["PATH"] = os.pathsep.join(keep)
    return env


def no_answer_trial(art, base, results):
    """Run the earlier copy's procedure on its seeded test files with no model answers, score it, and keep the score."""
    art.extractall(os.path.join(base, "earlier"))
    vp = os.path.join(base, "earlier", "verification_procedures")
    empty = os.path.join(base, "no_answers.json")
    with open(empty, "w") as f:
        f.write("{}\n")
    stream = P["nojudge_stream"]
    fx = os.path.join("fixtures", stream, "seeded")
    rundir = os.path.join("runs", "nojudge_" + stream)
    env = child_env(base)
    cmd = [sys.executable, "vg.py", "run", os.path.join("graphs", stream + ".yaml"), "--run", rundir, "--inputs", fx]
    for flag, name in (("--judge", "recorded_judge.json"), ("--second", "recorded_second.json")):
        if os.path.exists(os.path.join(vp, fx, name)):
            cmd += [flag, "recorded:" + empty]
    for args in (cmd, [sys.executable, "vg.py", "score", "--run", rundir, "--truth", os.path.join(fx, "truth.yaml")]):
        subprocess.run(args, cwd=vp, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    score = read_json(os.path.join(vp, rundir, "score.json"))
    results[stream + "_nojudge.faults"] = score["faults"]
    results[stream + "_nojudge.caught"] = len(score["caught"])


# step: Write table
def main():
    """Count every run, then the totals and comparisons, and write the table and the parameter record."""
    base = tempfile.mkdtemp(prefix="live_runs_")
    results = {}
    try:
        with tarfile.open(P["live_archive"]) as tf:
            tf.extractall(base)
            results["live.runs"] = len({m.name.split("/", 1)[0] for m in tf.getmembers()})
        runs = dict(pairs(P["live_runs"]))
        for label, folder in runs.items():
            one_run(os.path.join(base, folder), results, "live." + label + ".")
        for key in ("responses", "retries", "items"):
            results["live." + key] = sum(results["live." + label + "." + key] for label in runs)
        with tarfile.open(P["procedures_archive"]) as art:
            caught_all = faults_all = 0
            for label in P["judgment_runs"].split():
                run = os.path.join(base, runs[label])
                stream = read_json(os.path.join(run, "manifest.json"))["stream"]
                faults = judgment_faults(art, stream)
                caught = sum(flags(answer_of(run, f["check"], f["item"])) for f in faults)
                results["live." + label + ".judgment_faults"] = len(faults)
                results["live." + label + ".judgment_caught"] = caught
                faults_all += len(faults)
                caught_all += caught
            results["live.judgment_faults"] = faults_all
            results["live.judgment_caught"] = caught_all
            # Support verdicts of the live run against the recorded answers that come with the artifact.
            run = os.path.join(base, runs[P["differ_run"]])
            stream = read_json(os.path.join(run, "manifest.json"))["stream"]
            kind = P["differ_run"].rsplit(".", 1)[-1]
            recorded = json.load(art.extractfile(
                "verification_procedures/fixtures/" + stream + "/" + kind + "/recorded_judge.json"))
            no_answer_trial(art, base, results)
        step = P["support_step"]
        rows = answered_items(run, step)
        differ = 0
        for row in rows:
            live = answer_of(run, step, row) or {}
            if live.get("verdict") != (recorded.get(step + ":" + row) or {}).get("verdict"):
                differ += 1
        results["live.verdict_rows"] = len(rows)
        results["live.verdicts_differ"] = differ
        rechecks = answered_items(run, P["recheck_step"])
        results["live.rechecks"] = len(rechecks)
        results["live.rechecks_agree"] = sum((answer_of(run, P["recheck_step"], r) or {}).get("agree") is True
                                             for r in rechecks)
    finally:
        shutil.rmtree(base, ignore_errors=True)
    results_io.add_words(results, [k for k in P["word_keys"].split() if k in results],
                         [k for k in P["word_cap_keys"].split() if k in results])
    results_io.write_rows("live_runs.csv", results)
    P.write_record()


if __name__ == "__main__":
    main()
