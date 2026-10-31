"""Compute the appendix's numbers about the research artifact from its archive.

Purpose:
    Compute, from the archived research artifact alone, the numbers the
    appendix reports about the prototype. The archive is the artifact's newest
    public copy. It is unpacked twice into a temporary folder, one copy for the
    tests and one for the commands, so neither run can change what the other
    sees. Each test suite is run once and its passing tests are counted, in
    total and for named groups of test files. The A4 command blocks are run as
    the artifact's README gives them: the sample project's two builds, its data
    handoff and data run, and its phase handoff and data analysis run, then the
    references run, replayed and scored, then the prose and data runs, the
    three data phase reports, and the build run, each scored where the README
    scores it. What the commands print and what their run folders hold is kept.
    The figures of the A2.5 excerpt are read from the references run's own
    report and fields. What the appendix counts in the artifact's files is
    counted from the archive itself. Every number is one row of key and value,
    and a number the appendix writes as a word also gets a row with its word
    form.
Inputs:
    artifact_public_e22136c.tar - git archive of the newest public copy of the research artifact, at its commit e22136c.
Outputs:
    suite_counts.csv - tests passed in each suite, the number of suites, the total, and each named group.
    a4_results.csv - what the A4 command blocks report, and the figures of the A2.5 report excerpt.
    artifact_counts.csv - knowledge base entries, server tools, runtime commands, test-set sizes, tracked files and megabytes.
    params_record_artifact.csv - the parameters this run read, written by the run.
Parameters:
    artifact_archive - the archive of the research artifact.
    harness_programs - programs whose folders are left off the command path, so no test finds a real harness.
    suites - each suite as name=folder:target, run as pytest on target from that folder of the artifact.
    test_groups - named groups of test files as name=path,path, where a path ending in / takes a whole folder.
    slides_group - the group whose tests are searched for slide tests.
    slides_terms - words that mark a slide test in its class or test name.
    sample_project - the folder of the sample project that the A4 second block builds and checks.
    a4_runs - each A4 run on seeded test files as label=graph:folder, the folder under fixtures/ whose seeded test files it reads.
    judged_runs - the runs given the recorded answers that come with their test files.
    replayed_runs - the runs the verify command replays.
    scored_runs - the runs scored against the truth file of their test files.
    excerpt_stream - the run whose report A2.5 shows in part.
    excerpt_row - the entry the excerpt shows in full, when it is an AI citation with a located quote.
    excerpt_counts - the rows of the report's counts table as key=field, the field of fields.json that gives the row.
    hash_digits - how many characters of a checksum the excerpt prints.
    seeded_streams - the procedures whose test-set sizes are counted.
    fixture_kinds - the test-set folders of each procedure whose sizes are counted.
    kb_corpus - the folder of knowledge base entries, one subfolder per group.
    kb_server - the knowledge base server's file.
    kb_tool_call - the name of the call that declares one server tool.
    runtime_file - the runtime's file.
    command_call - the name of the call that declares one runtime command.
    bytes_per_mb - bytes in a megabyte.
    mb_digits - decimal places of the size in megabytes.
    word_keys - result keys that also get a word form.
    word_cap_keys - result keys that also get a word form starting with a capital.
Assumptions:
    Every command runs with every home the workflow reads (HOME, AUDIT_HOME,
    CONNECTIONS_HOME, FEATURES_HOME, XDG_CONFIG_HOME) inside the temporary
    folder, with VG_OFFLINE set, with no bytecode written, and without the
    folders that hold a harness program on the command path. Pandoc is on the
    command path for the sample builds. The A4 commands run from the folders
    the README names, with its relative paths, and a run on seeded test files
    writes to runs/demo_<graph>, as the README's runs do. A run's steps are the
    nodes of its graph, the steps it completes are the records it writes, and
    its replays are the lines of the verify command's output that say replay
    matches. A judged run's judged items are the items its judgment records say
    were put to the recorded answers, one request each in a live run. The
    excerpt omits the AI entries before and after the one shown, in the order
    of the report's headings, and every line of its Notes section. The
    excerpt's counts are the fields.json values excerpt_counts
    names, and the step stops when the report's counts table, its checksum of
    draft.md, or the heading of the entry shown in full disagree with
    fields.json. An entry is an AI citation with a located quote when its
    origin is ai and the passage step located a quote that a program found in
    its source. A test's outcome is read from the JUnit
    report pytest writes into the temporary folder, with the artifact as
    pytest's root folder, so each test's file is named from the artifact's top.
    No time, path, or version is written to an output. A suite that fails a
    test still gives its passed count, and its failed count is written too. A
    knowledge base entry describes software outside the artifact when the
    source named in its front matter is no file of the artifact. Test-set sizes
    count every file under each test-set folder in the archive.
"""
# step: Read parameters
import ast
import collections
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import xml.etree.ElementTree as ET

import yaml

import params_io
import results_io

P = params_io.Params(step="artifact", script="s1_artifact_numbers.py")
VP = "verification_procedures"
HOMES = ("HOME", "AUDIT_HOME", "CONNECTIONS_HOME", "FEATURES_HOME", "XDG_CONFIG_HOME")
VERSION_LINE = re.compile(r"^(v\S+) -> ", re.M)
Case = collections.namedtuple("Case", "suite file test outcome")


# step: Read files
def pairs(text):
    """Split a parameter written as name=value words into (name, value) pairs, in order."""
    return [tuple(word.split("=", 1)) for word in text.split()]


def read_json(path):
    """Read one JSON file."""
    with open(path) as f:
        return json.load(f)


def items_of(data):
    """Return the list of items of a findings or table file, whether it is a list or holds items."""
    return data["items"] if isinstance(data, dict) else data


def severities(path):
    """Count the findings of a run's findings file by severity."""
    return collections.Counter(f["severity"] for f in items_of(read_json(path)))


# step: Unpack
def unpack(archive, base, name):
    """Unpack the archive into the folder name inside base and return its path."""
    root = os.path.join(base, name)
    with tarfile.open(archive) as tf:
        tf.extractall(root)
    return root


def child_env(base):
    """Return the environment every command in the artifact runs with (see Assumptions)."""
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


def run(cmd, cwd, env):
    """Run one command with its output captured, not passed on, and return its standard output."""
    proc = subprocess.run(cmd, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          universal_newlines=True)
    return proc.stdout


# step: Run tests
def outcome(case):
    """Return passed, failed, or skipped for one testcase element of a JUnit report."""
    tags = {child.tag for child in case}
    if tags & {"failure", "error"}:
        return "failed"
    if "skipped" in tags:
        return "skipped"
    return "passed"


def run_suites(root, env, base):
    """Run each suite once with pytest and return one Case for every test it ran."""
    cases = []
    for name, spec in pairs(P["suites"]):
        folder, target = spec.split(":", 1)
        report = os.path.join(base, "junit_" + name + ".xml")
        run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--rootdir", root,
             "-o", "junit_family=xunit1", "--junitxml", report, target],
            os.path.join(root, folder), env)
        for case in ET.parse(report).iter("testcase"):
            cases.append(Case(name, case.get("file", ""),
                              case.get("classname", "") + "::" + case.get("name", ""), outcome(case)))
    return cases


def in_group(path, paths):
    """True when a test file is one of the group's files or lies in one of its folders."""
    return any(path == p or (p.endswith("/") and path.startswith(p)) for p in paths.split(","))


def suite_counts(cases):
    """Count passed tests by suite and by named group, plus failed and skipped by suite."""
    results = {}
    names = [name for name, _ in pairs(P["suites"])]
    for name in names:
        mine = [c for c in cases if c.suite == name]
        results["tests." + name] = sum(c.outcome == "passed" for c in mine)
        results["tests." + name + ".failed"] = sum(c.outcome == "failed" for c in mine)
        results["tests." + name + ".skipped"] = sum(c.outcome == "skipped" for c in mine)
    passed = [c for c in cases if c.outcome == "passed"]
    results["tests.suites"] = len(names)
    results["tests.total"] = len(passed)
    groups = dict(pairs(P["test_groups"]))
    for group, paths in groups.items():
        results["tests." + group] = sum(in_group(c.file, paths) for c in passed)
    terms = P["slides_terms"].lower().split()
    slide_paths = groups[P["slides_group"]]
    results["tests.slides"] = sum(in_group(c.file, slide_paths) and any(t in c.test.lower() for t in terms)
                                  for c in passed)
    return results


# step: A4 commands
def a4_runs():
    """Return each A4 run on seeded test files as label: (graph, folder under fixtures/), in order."""
    return {label: tuple(spec.split(":", 1)) for label, spec in pairs(P["a4_runs"])}


def demo(name):
    """Return the README's run folder runs/demo_<name>, relative to the procedures' folder."""
    return os.path.join("runs", "demo_" + name)


def judged_items(records):
    """Add up the items the judgment steps of a run put to a model or a recorded answer."""
    total = 0
    for name in sorted(os.listdir(records)):
        execution = read_json(os.path.join(records, name)).get("execution") or {}
        if execution.get("type") == "judgment":
            total += execution.get("items", 0)
    return total


def sample_block(root, env, results):
    """Run the A4 second block: the sample project's two builds, the data handoff and data run,
    and the phase handoff and the data analysis run with the sample's recorded answers."""
    sample = os.path.join(root, P["sample_project"])
    vp = os.path.join(root, VP)
    # The README's relative paths, from the sample project's folder and from the procedures' folder.
    project = os.path.relpath(sample, vp)
    handoffs = os.path.relpath(os.path.join(root, "handoffs"), vp)
    build = [sys.executable, "-m", "ospipe", "build"]
    build_env = dict(env, PYTHONPATH=os.path.relpath(os.path.join(root, "ospipe"), sample))
    run([sys.executable, "s1_results.py"], sample, env)
    out_m = run(build + ["--manuscript", "manuscript.md", "--manifest", "numbers.yml", "--tables-dir", ".",
                         "--bib", "refs.bib", "--builds-dir", "builds/manuscript", "--purpose", "sample manuscript"],
                sample, build_env)
    out_s = run(build + ["--manuscript", "slides.md", "--manifest", "numbers.yml", "--tables-dir", ".",
                         "--to", "revealjs", "--builds-dir", "builds/slides", "--purpose", "sample slides"],
                sample, build_env)
    versions = []
    for out in (out_m, out_s):
        found = VERSION_LINE.search(out)
        versions.append(found.group(1) if found else "none")
    results["sample.manuscript_version"], results["sample.slides_version"] = versions
    # One version when every build wrote the same one, otherwise each build's own.
    results["sample.version"] = "/".join(sorted(set(versions)))
    slides = os.path.join(sample, "builds", "slides", versions[-1] + ".html")
    with open(slides) as f:
        results["sample.slides"] = f.read().count("<section")
    run([sys.executable, os.path.join(handoffs, "project_to_data.py"), "--project", project,
         "--to", demo("sample_inputs")], vp, env)
    run([sys.executable, "vg.py", "run", os.path.join("graphs", "data.yaml"), "--run", demo("sample"),
         "--inputs", demo("sample_inputs")], vp, env)
    run([sys.executable, os.path.join(handoffs, "project_to_data_phases.py"), "--project", project,
         "--to", demo("sample_phases")], vp, env)
    run([sys.executable, "vg.py", "run", os.path.join("graphs", "data_analysis.yaml"), "--run",
         demo("sample_analysis"), "--inputs", demo("sample_phases"),
         "--judge", "recorded:" + os.path.join(project, "recorded_phases.json")], vp, env)
    files = os.path.join(vp, demo("sample"), "files")
    counts = severities(os.path.join(files, "findings.json"))
    results["sample.blocking"] = counts["blocking"]
    results["sample.warnings"] = counts["warning"]
    results["sample.notes"] = counts["info"]
    checked = items_of(read_json(os.path.join(files, "numbers_check.json")))
    results["sample.numbers"] = sum(bool(row.get("ok")) for row in checked)
    results["sample.numbers_listed"] = len(checked)
    fields = read_json(os.path.join(vp, demo("sample_analysis"), "files", "fields.json"))
    described = [it for it in fields["items"] if it.get("kind") == "description"]
    results["sample.analysis_steps"] = fields["run"]["n_steps"]
    results["sample.analysis_descriptions"] = len(described)
    results["sample.analysis_confirmed"] = sum(it.get("quote_found") is True and
                                               it.get("location_status") == "confirmed" for it in described)


def run_seeded(vp, env, label, graph, folder, results):
    """Run one procedure or phase report on its seeded test files as the README gives it, replay or
    score the run when params.yaml names it, and keep what it reports under the run's label."""
    inputs = os.path.join("fixtures", folder, "seeded")
    graph_file = os.path.join("graphs", graph + ".yaml")
    cmd = [sys.executable, "vg.py", "run", graph_file, "--run", demo(graph), "--inputs", inputs]
    if label in P["judged_runs"].split():
        cmd += ["--judge", "recorded:" + os.path.join(inputs, "recorded_judge.json")]
    run(cmd, vp, env)
    with open(os.path.join(vp, graph_file)) as f:
        results[label + ".steps"] = len(yaml.safe_load(f)["nodes"])
    records = os.path.join(vp, demo(graph), "records")
    results[label + ".steps_run"] = len([n for n in os.listdir(records) if n.endswith(".json")])
    if label in P["judged_runs"].split():
        results[label + ".judged"] = judged_items(records)
    if label in P["replayed_runs"].split():
        verify = run([sys.executable, "vg.py", "verify", "--run", demo(graph)], vp, env)
        results[label + ".replays"] = verify.count("replay matches")
    if label in P["scored_runs"].split():
        run([sys.executable, "vg.py", "score", "--run", demo(graph), "--truth", os.path.join(inputs, "truth.yaml")],
            vp, env)
        score = read_json(os.path.join(vp, demo(graph), "score.json"))
        results[label + ".faults"] = score["faults"]
        results[label + ".caught"] = len(score["caught"])
        results[label + ".missed"] = len(score["missed"])
        results[label + ".recall"] = score["recall"]
        results[label + ".extras"] = len(score["extra_findings"])


def a4_blocks(root, env):
    """Run the A4 second, third, and fourth blocks and return what they report, with the A2.5 excerpt."""
    results = {}
    vp = os.path.join(root, VP)
    sample_block(root, env, results)
    for label, (graph, folder) in a4_runs().items():
        run_seeded(vp, env, label, graph, folder, results)
    excerpt(vp, results)
    return results


# step: Report excerpt
def counts_table(report):
    """Return the numbers of a report's counts table, the one headed Count and Number, in its order."""
    numbers, inside = [], False
    for line in report.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not inside:
            inside = cells == ["Count", "Number"]
        elif not line.startswith("|"):
            break
        elif set(cells[-1]) - set("-"):
            # Every row but the line of dashes under the heading.
            numbers.append(int(cells[-1]))
    return numbers


def section_bullets(report, heading):
    """Return the bullet lines of one ## section of a report."""
    bullets, inside = [], False
    for line in report.splitlines():
        if line.startswith("## "):
            inside = line[len("## "):].strip() == heading
        elif inside and line.startswith("- "):
            bullets.append(line)
    return bullets


def located(quote):
    """True when the passage step located a quote, not a section pointer, that a program found in the source."""
    return quote.get("from") == "located" and quote.get("kind") == "quote" and quote.get("in_source") == "yes"


def excerpt(vp, results):
    """Keep the figures the A2.5 excerpt prints from the references run's own report.md and fields.json."""
    files = os.path.join(vp, demo(a4_runs()[P["excerpt_stream"]][0]), "files")
    fields = read_json(os.path.join(files, "fields.json"))
    with open(os.path.join(files, "report.md")) as f:
        report = f.read()
    head, digits = fields["run"], P["hash_digits"]
    named = pairs(P["excerpt_counts"])
    ai = [it for it in fields["items"] if it.get("origin") == "ai"]
    # The entry shown in full is excerpt_row when it is an AI citation with a located quote, else the first such.
    entries = [it for it in ai if any(located(q) for q in it.get("quotes") or [])]
    entry = ([it for it in entries if it["id"] == P["excerpt_row"]] or entries)[0]
    # The report is written from its fields, so the two must agree on what the excerpt shows.
    if (counts_table(report) != [head[field] for _, field in named] or head["draft_sha256"] not in report
            or "### " + entry["heading"] not in report):
        raise ValueError("report.md and fields.json of the excerpt's run disagree")
    results["excerpt.doc_sha"] = head["draft_sha256"].split(":")[-1][:digits]
    for key, field in named:
        results["excerpt." + key] = head[field]
    results["excerpt.row"] = entry["id"]
    results["excerpt.row_source_sha"] = entry["source_sha256"].split(":")[-1][:digits]
    results["excerpt.row_location"] = [q for q in entry["quotes"] if located(q)][0]["location"]
    # The AI entries the excerpt omits before and after the one shown, in the report's order of headings.
    ai_ids = {it["id"] for it in ai}
    order = [h for h in re.findall(r"^### (\S+):", report, re.M) if h in ai_ids]
    at = order.index(entry["id"])
    results["excerpt.ai_before"] = at
    results["excerpt.ai_after"] = len(order) - at - 1
    results["excerpt.notes_omitted"] = len(section_bullets(report, "Notes"))


# step: Count files
def front_matter(text):
    """Return the name: value lines of a markdown file's opening block between --- lines."""
    lines = text.splitlines()
    out = {}
    if lines[:1] == ["---"]:
        for line in lines[1:]:
            if line.strip() == "---":
                break
            key, _, value = line.partition(":")
            out[key.strip()] = value.strip()
    return out


def count_calls(source, name):
    """Count the calls in Python source whose function is name, alone or as an attribute."""
    total = 0
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Call):
            f = node.func
            if (isinstance(f, ast.Name) and f.id == name) or (isinstance(f, ast.Attribute) and f.attr == name):
                total += 1
    return total


def archive_counts(archive):
    """Count what the appendix counts in the archive's files, without running anything."""
    results = {}
    with tarfile.open(archive) as tf:
        members = [m for m in tf.getmembers() if m.isfile()]
        names = {m.name for m in members}

        def text(name):
            """Return one archived file's text."""
            return tf.extractfile(name).read().decode("utf-8")

        results["repo.files"] = len(members)
        size = sum(m.size for m in members) / P["bytes_per_mb"]
        results["repo.mb"] = "{0:.{1}f}".format(size, P["mb_digits"])
        corpus = P["kb_corpus"].rstrip("/") + "/"
        entries = sorted(n for n in names
                         if n.startswith(corpus) and n.endswith(".md") and n[len(corpus):].count("/") == 1)
        results["kb.entries"] = len(entries)
        outside = 0
        for name in entries:
            source = front_matter(text(name)).get("source", "")
            # Outside when no file of the artifact is the source the entry names.
            if not any(n == source or n.endswith("/" + source) for n in names):
                outside += 1
        results["kb.outside"] = outside
        results["kb.tools"] = count_calls(text(P["kb_server"]), P["kb_tool_call"])
        results["runtime.commands"] = count_calls(text(P["runtime_file"]), P["command_call"])
        sizes = []
        for stream in P["seeded_streams"].split():
            for kind in P["fixture_kinds"].split():
                prefix = "/".join((VP, "fixtures", stream, kind)) + "/"
                sizes.append(sum(n.startswith(prefix) for n in names))
        results["fixtures.min_files"] = min(sizes)
        results["fixtures.max_files"] = max(sizes)
    return results


# step: Write tables
def main():
    """Compute every number, add the word forms, and write the three tables and the parameter record."""
    archive = P["artifact_archive"]
    counts = archive_counts(archive)
    # The real path, since pytest names a test's file relative to its root folder only when
    # both are spelled the same way, and macOS reaches the temporary folder through a link.
    base = os.path.realpath(tempfile.mkdtemp(prefix="artifact_numbers_"))
    try:
        env = child_env(base)
        suites = suite_counts(run_suites(unpack(archive, base, "suites"), env, base))
        a4 = a4_blocks(unpack(archive, base, "commands"), env)
    finally:
        shutil.rmtree(base, ignore_errors=True)
    words, caps = P["word_keys"].split(), P["word_cap_keys"].split()
    for results in (suites, a4, counts):
        results_io.add_words(results, [k for k in words if k in results], [k for k in caps if k in results])
    results_io.write_rows("suite_counts.csv", suites)
    results_io.write_rows("a4_results.csv", a4)
    results_io.write_rows("artifact_counts.csv", counts)
    P.write_record()


if __name__ == "__main__":
    main()
