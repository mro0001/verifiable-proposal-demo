# AI sessions of verifiable_proposal_demo

This folder lists every AI session that touched the project verifiable_proposal_demo, 181 AI sessions in all, and 19 of them led to an AI contribution in the final verification reports. A session touched the project when it ran in the project's folder or when one of its tool calls read, edited, or wrote a file inside it. A session that made a contribution in the final reports is listed too, wherever it ran. The audit layer wrote the folder with `python3 -m audit_layer write-out session-index`.

## What the index holds

- `sessions.csv`, one row for each session.
- `index.html`, the same rows on one page, with a search box.
- One page for each session, named by its public id.
- For each session, its public id, its start and its length in minutes, the harness and its version, the models that answered in it, and, for a subagent, the public id of the session that started it.
- Its tool calls counted by verb, and the project files it read, edited, and wrote, each named relative to the project folder.
- The sha256 and the size in bytes of its transcript.
- The title, gist, summary, and keywords a model wrote for the session. Each session marks them as written by a model, and as not reviewed by the author unless a person reviewed them. In them only the home folder's path is written as ~, and each term on the author's list as [withheld], so they may name other files and full paths.
- The session's AI contributions that reached the final verification reports. Each has a reference id, the stream and the item, such as `citations/r02`. The stream's report and results file name the same item with the same public id. Beside each is the run of the results file and the decision recorded for the item, approved, held, not yet decided, or needs no decision.

## What the index does not hold

- No transcript text, prompt, or tool output. The transcripts stay private.
- No file outside the project named in the file fields, the project files read, edited, and written. Such files are counted and never named.
- No full path in the file fields.
- The title, gist, summary, and keywords a model wrote are not held to this. They may name other files and full paths, and in them only the home folder's path and the terms on the author's list are replaced.
- No harness's own id for a session. A public id is S followed by the first 12 hex characters of the sha256 of that id, which cannot be turned back into it.

## Checking a transcript against its checksum

A transcript shared later can be checked against its session's row. Its sha256 must equal the row's `transcript_sha256`, and its size in bytes the row's `transcript_bytes`.

```
shasum -a 256 TRANSCRIPT
wc -c < TRANSCRIPT
```

The session's public id can be worked out from the session id the transcript names. It is S followed by the 12 characters this prints.

```
printf '%s' 'SESSION ID' | shasum -a 256 | cut -c1-12
```

The checksum is that of the transcript as the audit layer last stored it.

## Searching the index

GitHub shows `sessions.csv` as a table with a search box. [index.html](index.html) shows the rows on one page with a search box and a checkbox, "Only sessions with an AI contribution in the final reports". It opens in a browser from disk, and from GitHub Pages when the repository publishes this folder.

## Sessions

| Session | Started | Minutes | Harness | Title | AI contributions in the final reports |
|---|---|---|---|---|---|
| [Sf2b3ddaba981](Sf2b3ddaba981.md) | 2026-09-10T15:42:31.222Z | 7651.9 | claude_code |  | 11 |
| [S1fc10e437250](S1fc10e437250.md) | 2026-09-10T16:48:20.048Z | 3.5 | claude_code |  | 1 |
| [S4fe08bc23803](S4fe08bc23803.md) | 2026-09-10T17:59:38.371Z | 2.5 | claude_code |  | 2 |
| [Sfdc8140a6627](Sfdc8140a6627.md) | 2026-09-10T18:35:39.753Z | 0.5 | claude_code |  | 5 |
| [Sf82d13eab9b1](Sf82d13eab9b1.md) | 2026-09-10T20:35:38.653Z | 1.3 | claude_code |  | 0 |
| [Sd833c6cb59ec](Sd833c6cb59ec.md) | 2026-09-10T20:35:40.358Z | 4.1 | claude_code |  | 0 |
| [S78607384d855](S78607384d855.md) | 2026-09-10T20:35:40.359Z | 2.0 | claude_code |  | 0 |
| [S9be4d75f59c9](S9be4d75f59c9.md) | 2026-09-10T20:35:40.359Z | 2.9 | claude_code |  | 0 |
| [S3577809ec6cd](S3577809ec6cd.md) | 2026-09-10T20:42:42.170Z | 4.4 | claude_code |  | 0 |
| [Sc28fc5f9e36c](Sc28fc5f9e36c.md) | 2026-09-10T20:42:43.463Z | 1.8 | claude_code |  | 0 |
| [S11001a3d457f](S11001a3d457f.md) | 2026-09-10T20:42:43.464Z | 1.1 | claude_code |  | 0 |
| [S36f3a9b5978e](S36f3a9b5978e.md) | 2026-09-10T21:26:08.774Z | 5.3 | claude_code |  | 0 |
| [S91d4c0fbda9c](S91d4c0fbda9c.md) | 2026-09-10T21:26:10.259Z | 1.3 | claude_code |  | 0 |
| [S219b893c5544](S219b893c5544.md) | 2026-09-10T21:26:10.259Z | 3.8 | claude_code |  | 0 |
| [S3a5afcbf25e4](S3a5afcbf25e4.md) | 2026-09-10T21:26:10.260Z | 1.7 | claude_code |  | 0 |
| [Sd457d8e4313a](Sd457d8e4313a.md) | 2026-09-15T21:53:43.682Z | 3.5 | claude_code |  | 0 |
| [Se40d6673f69b](Se40d6673f69b.md) | 2026-09-17T19:09:54.833Z | 1465.4 | claude_code |  | 0 |
| [Scbb22ae805e2](Scbb22ae805e2.md) | 2026-09-23T19:24:50.319Z | 7086.9 | claude_code |  | 0 |
| [Sc6b2052f13b0](Sc6b2052f13b0.md) | 2026-09-23T20:07:30.934Z | 6.7 | claude_code |  | 0 |
| [S42812eb01e05](S42812eb01e05.md) | 2026-09-24T17:18:42.370Z | 7.9 | claude_code |  | 2 |
| [Sa41d678f3e51](Sa41d678f3e51.md) | 2026-09-28T17:51:00.614Z | 9.5 | claude_code |  | 0 |
| [S2c62c2036e7b](S2c62c2036e7b.md) | 2026-09-28T20:21:53.011Z | 2777.9 | claude_code |  | 5 |
| [Sae95a1bc7281](Sae95a1bc7281.md) | 2026-09-28T20:35:50.651Z | 15.7 | claude_code |  | 1 |
| [S3041cff31f75](S3041cff31f75.md) | 2026-09-28T20:35:52.184Z | 14.5 | claude_code |  | 1 |
| [Sde6d6e4c7742](Sde6d6e4c7742.md) | 2026-09-28T20:35:52.184Z | 18.1 | claude_code |  | 1 |
| [S93db6145969b](S93db6145969b.md) | 2026-09-28T20:35:52.185Z | 13.5 | claude_code |  | 0 |
| [S13f82894206c](S13f82894206c.md) | 2026-09-28T20:35:52.185Z | 16.8 | claude_code |  | 0 |
| [Seb2bc9109e65](Seb2bc9109e65.md) | 2026-09-28T20:35:52.185Z | 11.2 | claude_code |  | 0 |
| [S359af1f0da52](S359af1f0da52.md) | 2026-09-28T20:35:52.185Z | 13.2 | claude_code |  | 0 |
| [Sf34b09a6a76a](Sf34b09a6a76a.md) | 2026-09-28T20:35:52.185Z | 10.8 | claude_code |  | 0 |
| [S7376841eb514](S7376841eb514.md) | 2026-09-28T20:56:50.505Z | 18.7 | claude_code |  | 0 |
| [S873a67f748e7](S873a67f748e7.md) | 2026-09-28T20:56:51.735Z | 19.6 | claude_code |  | 0 |
| [Sa161f41c0ec3](Sa161f41c0ec3.md) | 2026-09-28T20:56:51.735Z | 20.9 | claude_code |  | 0 |
| [S1366a4c5d79c](S1366a4c5d79c.md) | 2026-09-28T21:17:46.811Z | 8.2 | claude_code |  | 0 |
| [Sc5a8f2c0a9d7](Sc5a8f2c0a9d7.md) | 2026-09-28T21:17:47.644Z | 9.4 | claude_code |  | 0 |
| [S2aeaaecf421d](S2aeaaecf421d.md) | 2026-09-28T21:17:47.644Z | 10.8 | claude_code |  | 0 |
| [S853c268f4d47](S853c268f4d47.md) | 2026-09-28T21:28:37.922Z | 23.3 | claude_code |  | 0 |
| [Sdfb8e9e0d923](Sdfb8e9e0d923.md) | 2026-09-28T21:54:05.195Z | 8.7 | claude_code |  | 0 |
| [Sa48a0ca6db26](Sa48a0ca6db26.md) | 2026-09-28T21:54:06.635Z | 9.5 | claude_code |  | 0 |
| [See3316d6473a](See3316d6473a.md) | 2026-09-28T21:54:06.636Z | 12.2 | claude_code |  | 0 |
| [S96e83f005086](S96e83f005086.md) | 2026-09-28T21:54:06.636Z | 10.5 | claude_code |  | 0 |
| [S9e0492bef3a2](S9e0492bef3a2.md) | 2026-09-28T21:54:06.636Z | 21.0 | claude_code |  | 0 |
| [S9d4e0ac3bff5](S9d4e0ac3bff5.md) | 2026-09-28T21:54:06.636Z | 11.3 | claude_code |  | 0 |
| [S870c155998a7](S870c155998a7.md) | 2026-09-28T21:54:06.636Z | 4.3 | claude_code |  | 0 |
| [Se57fd58ee65c](Se57fd58ee65c.md) | 2026-09-28T22:15:06.839Z | 20.7 | claude_code |  | 0 |
| [S00b2ba25cb06](S00b2ba25cb06.md) | 2026-09-28T22:35:51.335Z | 6.8 | claude_code |  | 0 |
| [Sf37d53a00a5b](Sf37d53a00a5b.md) | 2026-09-30T17:13:39.962Z | 2.9 | claude_code |  | 0 |
| [Sc9fee6178d98](Sc9fee6178d98.md) | 2026-09-30 18:56:13.739232 | 1577.6 | forgecode |  | 0 |
| [S053cdd36d144](S053cdd36d144.md) | 2026-09-30 19:27:22.790818 | 0.5 | forgecode |  | 0 |
| [Se9e33f050caf](Se9e33f050caf.md) | 2026-09-30 19:45:09.624191 | 0.0 | forgecode |  | 0 |
| [Sa1460b5f0c2e](Sa1460b5f0c2e.md) | 2026-09-30 19:51:03.253197 | 2.7 | forgecode |  | 0 |
| [S899954f4b5ec](S899954f4b5ec.md) | 2026-09-30 19:54:37.784145 | 3.8 | forgecode |  | 0 |
| [S2ff391680aec](S2ff391680aec.md) | 2026-09-30 20:12:27.972482 | 0.2 | forgecode |  | 0 |
| [Scb01b5fcb183](Scb01b5fcb183.md) | 2026-09-30 20:12:27.973386 | 0.4 | forgecode |  | 0 |
| [S76bdc512515c](S76bdc512515c.md) | 2026-09-30 21:54:24.599640 | 0.3 | forgecode |  | 0 |
| [S9183e233a4e3](S9183e233a4e3.md) | 2026-09-30 21:54:44.825397 | 0.3 | forgecode |  | 0 |
| [S6c6f9bb9fb5b](S6c6f9bb9fb5b.md) | 2026-09-30 22:07:25.027028 | 0.6 | forgecode |  | 0 |
| [Sadd5384f726f](Sadd5384f726f.md) | 2026-09-30 22:07:31.410410 | 0.4 | forgecode |  | 0 |
| [Sada8afeaf14e](Sada8afeaf14e.md) | 2026-09-30 22:08:08.986699 | 3.5 | forgecode |  | 0 |
| [Se58625d98cc2](Se58625d98cc2.md) | 2026-09-30 22:10:29.433283 | 0.1 | forgecode |  | 0 |
| [Sf9d949855f97](Sf9d949855f97.md) | 2026-09-30 22:21:00.420024 | 0.7 | forgecode |  | 0 |
| [S2f05dc173fd9](S2f05dc173fd9.md) | 2026-09-30 22:58:58.762684 | 0.0 | forgecode |  | 0 |
| [Sde820bcb80fc](Sde820bcb80fc.md) | 2026-09-30 22:58:58.762709 | 5.5 | forgecode |  | 0 |
| [S42e79e4b5ec0](S42e79e4b5ec0.md) | 2026-09-30 22:58:58.762776 | 0.3 | forgecode |  | 0 |
| [S6f26f03f3731](S6f26f03f3731.md) | 2026-09-30 22:58:58.762793 | 0.2 | forgecode |  | 0 |
| [S43f2ac71653c](S43f2ac71653c.md) | 2026-09-30 22:58:58.763513 | 0.2 | forgecode |  | 0 |
| [Sc8ca7e6ab73b](Sc8ca7e6ab73b.md) | 2026-09-30 22:58:58.763596 | 0.1 | forgecode |  | 0 |
| [Sc550a82d4b2d](Sc550a82d4b2d.md) | 2026-09-30 22:58:58.763605 | 0.1 | forgecode |  | 0 |
| [Sbdcb3e08d165](Sbdcb3e08d165.md) | 2026-09-30 22:58:58.763641 | 0.2 | forgecode |  | 0 |
| [S0af97f15a9bd](S0af97f15a9bd.md) | 2026-09-30 22:58:58.763731 | 0.2 | forgecode |  | 0 |
| [S7202ba404562](S7202ba404562.md) | 2026-09-30 22:58:58.763816 | 0.2 | forgecode |  | 0 |
| [Se563cfbb80b1](Se563cfbb80b1.md) | 2026-09-30 23:34:16.399930 | 0.9 | forgecode |  | 0 |
| [Sd95fb5da0323](Sd95fb5da0323.md) | 2026-10-01 19:03:23.865811 | 0.1 | forgecode |  | 0 |
| [Sc834e7477db4](Sc834e7477db4.md) | 2026-10-01 21:01:56.321484 | 0.7 | forgecode |  | 0 |
| [S90ee9cd65666](S90ee9cd65666.md) | 2026-10-01 21:15:41.993124 | 41.9 | forgecode |  | 0 |
| [Se3eef308a3bd](Se3eef308a3bd.md) | 2026-10-01 21:28:54.749930 | 2.0 | forgecode |  | 0 |
| [S26cfc250a733](S26cfc250a733.md) | 2026-10-01T21:58:21.669Z | 5458.4 | claude_code |  | 1 |
| [S35fa53ceae19](S35fa53ceae19.md) | 2026-10-01 23:28:40.705800 | 5.5 | forgecode |  | 0 |
| [S4e649baca937](S4e649baca937.md) | 2026-10-02 01:03:34.690034 | 28.0 | forgecode |  | 0 |
| [S8c51c1b6103f](S8c51c1b6103f.md) | 2026-10-02T02:47:12.957Z | 18.2 | claude_code |  | 0 |
| [S75c6ddbe0853](S75c6ddbe0853.md) | 2026-10-02T02:47:29.492Z | 20.4 | claude_code |  | 1 |
| [S2bc62321d9c9](S2bc62321d9c9.md) | 2026-10-02T02:47:46.007Z | 16.7 | claude_code |  | 0 |
| [S8f1dafba2be7](S8f1dafba2be7.md) | 2026-10-02T02:48:02.706Z | 21.3 | claude_code |  | 0 |
| [S35d5ba7e088a](S35d5ba7e088a.md) | 2026-10-05T17:36:07.118Z | 3797.8 | claude_code |  | 1 |
| [S387aedb1c5df](S387aedb1c5df.md) | 2026-10-05T17:41:11.028Z | 1.5 | claude_code |  | 0 |
| [S68b73aca10c9](S68b73aca10c9.md) | 2026-10-08T07:13:46.349Z | 0.2 | claude_code |  | 0 |
| [S3243b86596e9](S3243b86596e9.md) | 2026-10-08T08:43:40.466Z | 1.0 | claude_code |  | 0 |
| [S0a0b07250554](S0a0b07250554.md) | 2026-10-08T17:45:39.573Z | 29.1 | claude_code |  | 0 |
| [Sdc2ad47b884a](Sdc2ad47b884a.md) | 2026-10-08T17:56:50.475Z | 7.1 | claude_code |  | 0 |
| [S05919e1bfcc6](S05919e1bfcc6.md) | 2026-10-08T17:57:22.234Z | 2.8 | claude_code |  | 0 |
| [S92f69da35825](S92f69da35825.md) | 2026-10-08T17:57:30.296Z | 4.2 | claude_code |  | 0 |
| [S4420117a098c](S4420117a098c.md) | 2026-10-08T17:57:38.839Z | 2.9 | claude_code |  | 0 |
| [Sd29899155f2b](Sd29899155f2b.md) | 2026-10-08T17:57:47.760Z | 3.2 | claude_code |  | 0 |
| [Scffaf35dce3e](Scffaf35dce3e.md) | 2026-10-08T18:49:49.309Z | 4404.4 | claude_code |  | 0 |
| [Scecd89f9bc5b](Scecd89f9bc5b.md) | 2026-10-09T16:55:08.768Z | 1.0 | claude_code |  | 1 |
| [S64646222b4c4](S64646222b4c4.md) | 2026-10-22T19:50:49.962Z | 1426.8 | claude_code |  | 1 |
| [S76241aa0b6b1](S76241aa0b6b1.md) | 2026-10-22T21:57:51.765Z | 1.9 | claude_code |  | 0 |
| [S1b7969972487](S1b7969972487.md) | 2026-10-22T22:57:33.500Z | 4.6 | claude_code |  | 0 |
| [S8e356c2cb3c0](S8e356c2cb3c0.md) | 2026-10-23T02:26:34.200Z | 9.5 | claude_code |  | 0 |
| [S600454036c21](S600454036c21.md) | 2026-10-23T03:37:27.973Z | 5.3 | claude_code |  | 0 |
| [Se2a39258dacf](Se2a39258dacf.md) | 2026-10-23T03:45:54.528Z | 6.8 | claude_code |  | 0 |
| [S2934df0a9e27](S2934df0a9e27.md) | 2026-10-23T18:02:23.002Z | 3.9 | claude_code |  | 1 |
| [S0aedfdf592f9](S0aedfdf592f9.md) | 2026-10-23T18:02:47.114Z | 4.2 | claude_code |  | 0 |
| [Sf4ea29931912](Sf4ea29931912.md) | 2026-10-23T21:02:30.535Z | 5923.4 | claude_code |  | 0 |
| [Sa740c1a5c96f](Sa740c1a5c96f.md) | 2026-10-23T21:12:15.528Z | 20.4 | claude_code |  | 0 |
| [Sb89945be3808](Sb89945be3808.md) | 2026-10-23T21:12:18.577Z | 24.8 | claude_code |  | 0 |
| [S794b06fb2e44](S794b06fb2e44.md) | 2026-10-23T21:12:18.578Z | 23.4 | claude_code |  | 0 |
| [S7fc98fd157ad](S7fc98fd157ad.md) | 2026-10-23T21:12:18.578Z | 25.5 | claude_code |  | 0 |
| [S1c818d80823f](S1c818d80823f.md) | 2026-10-23T21:12:18.579Z | 23.9 | claude_code |  | 0 |
| [S8c193d1cd498](S8c193d1cd498.md) | 2026-10-23T21:12:18.579Z | 19.4 | claude_code |  | 0 |
| [S42afa29c875d](S42afa29c875d.md) | 2026-10-23T21:12:18.580Z | 22.1 | claude_code |  | 0 |
| [Sb172d28a977a](Sb172d28a977a.md) | 2026-10-23T21:12:18.580Z | 29.8 | claude_code |  | 0 |
| [S7ee5edc6d38c](S7ee5edc6d38c.md) | 2026-10-23T21:12:18.580Z | 37.8 | claude_code |  | 0 |
| [S117ef23913bf](S117ef23913bf.md) | 2026-10-23T21:52:45.674Z | 19.8 | claude_code |  | 0 |
| [S964bcb62679b](S964bcb62679b.md) | 2026-10-23T21:52:48.822Z | 20.4 | claude_code |  | 0 |
| [Sddec8cb45e0d](Sddec8cb45e0d.md) | 2026-10-23T21:52:48.822Z | 23.1 | claude_code |  | 0 |
| [S195a13894555](S195a13894555.md) | 2026-10-23T22:15:53.085Z | 9.9 | claude_code |  | 0 |
| [Sdf7f1f86ed17](Sdf7f1f86ed17.md) | 2026-10-23T22:15:56.129Z | 11.8 | claude_code |  | 0 |
| [S4e1858f19c01](S4e1858f19c01.md) | 2026-10-23T22:15:56.130Z | 10.1 | claude_code |  | 0 |
| [S0be70297055a](S0be70297055a.md) | 2026-10-23T22:27:46.514Z | 28.7 | claude_code |  | 0 |
| [Sc256a71a98c0](Sc256a71a98c0.md) | 2026-10-23T23:03:00.094Z | 22.6 | claude_code |  | 0 |
| [S32b53da2f560](S32b53da2f560.md) | 2026-10-23T23:03:03.760Z | 17.5 | claude_code |  | 0 |
| [S1325474732fb](S1325474732fb.md) | 2026-10-23T23:03:03.761Z | 23.1 | claude_code |  | 0 |
| [Sffbd51119cff](Sffbd51119cff.md) | 2026-10-23T23:03:03.762Z | 22.7 | claude_code |  | 0 |
| [Scc3b8d4a760c](Scc3b8d4a760c.md) | 2026-10-23T23:26:11.260Z | 18.7 | claude_code |  | 0 |
| [Sb065ab2a1ddb](Sb065ab2a1ddb.md) | 2026-10-23T23:49:26.165Z | 33.9 | claude_code |  | 0 |
| [S73a98c2d4d38](S73a98c2d4d38.md) | 2026-10-23T23:49:29.189Z | 29.0 | claude_code |  | 0 |
| [Sf2db7e615e45](Sf2db7e615e45.md) | 2026-10-23T23:49:29.189Z | 21.2 | claude_code |  | 0 |
| [S02a7b5a8163c](S02a7b5a8163c.md) | 2026-10-23T23:49:29.189Z | 20.7 | claude_code |  | 0 |
| [S8a97d1399481](S8a97d1399481.md) | 2026-10-23T23:49:29.190Z | 21.2 | claude_code |  | 0 |
| [Sd0411629f08c](Sd0411629f08c.md) | 2026-10-23T23:49:29.190Z | 26.1 | claude_code |  | 0 |
| [Sf06c63671b45](Sf06c63671b45.md) | 2026-10-23T23:49:29.191Z | 26.4 | claude_code |  | 0 |
| [Sc4f5090ea6d2](Sc4f5090ea6d2.md) | 2026-10-24T00:23:20.656Z | 35.3 | claude_code |  | 0 |
| [S04eb8407259a](S04eb8407259a.md) | 2026-10-24T01:26:09.537Z | 22.7 | claude_code |  | 0 |
| [S025295163f04](S025295163f04.md) | 2026-10-24T01:42:19.625Z | 13.6 | claude_code |  | 0 |
| [Sbb982c726559](Sbb982c726559.md) | 2026-10-24T01:42:22.738Z | 18.9 | claude_code |  | 0 |
| [S856d625931b1](S856d625931b1.md) | 2026-10-24T01:42:22.738Z | 22.0 | claude_code |  | 0 |
| [S7568c518a162](S7568c518a162.md) | 2026-10-24T01:42:22.738Z | 18.3 | claude_code |  | 0 |
| [Sec12e83f9e78](Sec12e83f9e78.md) | 2026-10-24T01:42:22.738Z | 19.3 | claude_code |  | 0 |
| [Sf405afbb18ce](Sf405afbb18ce.md) | 2026-10-24T01:42:22.738Z | 17.5 | claude_code |  | 0 |
| [Sd6ffcde8d687](Sd6ffcde8d687.md) | 2026-10-24T01:48:51.536Z | 15.9 | claude_code |  | 0 |
| [S240c8df378ae](S240c8df378ae.md) | 2026-10-24T01:48:54.892Z | 16.6 | claude_code |  | 0 |
| [Sa43f28f5160d](Sa43f28f5160d.md) | 2026-10-24T02:04:23.522Z | 20.1 | claude_code |  | 0 |
| [S7c4850a6d5db](S7c4850a6d5db.md) | 2026-10-24T02:24:29.847Z | 41.1 | claude_code |  | 0 |
| [S2d832dec00ae](S2d832dec00ae.md) | 2026-10-24T03:05:38.014Z | 23.9 | claude_code |  | 0 |
| [Sa5d83ce7a032](Sa5d83ce7a032.md) | 2026-10-24T05:32:44.234Z | 36.9 | claude_code |  | 0 |
| [Sd8f213a7c401](Sd8f213a7c401.md) | 2026-10-24T05:32:44.234Z | 36.9 | claude_code |  | 0 |
| [S3f4b2f802b4c](S3f4b2f802b4c.md) | 2026-10-26T18:13:38.905Z | 3.3 | claude_code |  | 0 |
| [S09c9c70943bd](S09c9c70943bd.md) | 2026-10-26T18:13:42.542Z | 4.1 | claude_code |  | 0 |
| [Sec0bf0a18e34](Sec0bf0a18e34.md) | 2026-10-26T18:13:42.542Z | 5.4 | claude_code |  | 0 |
| [S2f2f786f84f1](S2f2f786f84f1.md) | 2026-10-26T18:13:42.542Z | 3.6 | claude_code |  | 0 |
| [S23a5cafa204d](S23a5cafa204d.md) | 2026-10-26T18:13:42.542Z | 4.7 | claude_code |  | 0 |
| [Sc8d3a0197938](Sc8d3a0197938.md) | 2026-10-26T18:33:25.891Z | 5.1 | claude_code |  | 0 |
| [Sf6719b42155e](Sf6719b42155e.md) | 2026-10-26T18:33:25.892Z | 3.5 | claude_code |  | 0 |
| [S0417d0808172](S0417d0808172.md) | 2026-10-26T18:33:25.893Z | 3.7 | claude_code |  | 0 |
| [S25d5d1a4580a](S25d5d1a4580a.md) | 2026-10-26T19:31:31.294Z | 5.2 | claude_code |  | 0 |
| [Sf217fe0e2d97](Sf217fe0e2d97.md) | 2026-10-26T19:31:34.395Z | 7.3 | claude_code |  | 0 |
| [S74fc4d297c47](S74fc4d297c47.md) | 2026-10-26T19:31:34.395Z | 4.7 | claude_code |  | 0 |
| [Sf9cfe3e02173](Sf9cfe3e02173.md) | 2026-10-26T19:31:34.396Z | 4.3 | claude_code |  | 0 |
| [S7482d3a2fb99](S7482d3a2fb99.md) | 2026-10-26T21:27:30.558Z | 8.0 | claude_code |  | 0 |
| [S8ae3a7fcfd8b](S8ae3a7fcfd8b.md) | 2026-10-26T21:27:39.639Z | 5.4 | claude_code |  | 0 |
| [Sc5efb6aca7f6](Sc5efb6aca7f6.md) | 2026-10-26T22:06:18.815Z | 9.1 | claude_code |  | 0 |
| [S9d1933f0442c](S9d1933f0442c.md) | 2026-10-26T22:06:30.650Z | 7.3 | claude_code |  | 0 |
| [S6e3375714e12](S6e3375714e12.md) | 2026-10-27T06:30:11.275Z | 13.4 | claude_code |  | 0 |
| [S47c485d664ce](S47c485d664ce.md) | 2026-10-27T06:30:28.922Z | 13.6 | claude_code |  | 0 |
| [S807c28519e22](S807c28519e22.md) | 2026-10-27T06:30:44.875Z | 9.0 | claude_code |  | 0 |
| [Sc1a0850f7985](Sc1a0850f7985.md) | 2026-10-27T06:31:02.012Z | 15.2 | claude_code |  | 0 |
| [S52c9f6be66e7](S52c9f6be66e7.md) | 2026-10-27T06:47:07.953Z | 30.0 | claude_code |  | 0 |
| [S4f3028e22164](S4f3028e22164.md) | 2026-10-27T17:10:15.238Z | 4.0 | claude_code |  | 0 |
| [Scf5b1ab110e3](Scf5b1ab110e3.md) | 2026-10-27T20:22:53.238Z | 8.1 | claude_code |  | 0 |
| [Sef8bc4dfeadb](Sef8bc4dfeadb.md) | 2026-10-27T20:23:12.695Z | 8.8 | claude_code |  | 0 |
| [S1055c139a902](S1055c139a902.md) | 2026-10-28T00:02:13.889Z | 1030.7 | claude_code |  | 0 |
| [S921f30753997](S921f30753997.md) | 2026-10-30T17:34:14.576Z | 12.5 | claude_code |  | 0 |
| [Sea91e4086425](Sea91e4086425.md) | 2026-10-30T17:46:46.267Z | 12.7 | claude_code |  | 81 |
| [Sac8f67131af4](Sac8f67131af4.md) | 2026-10-30T17:59:27.776Z | 6.7 | claude_code | Review of verifiable_proposal_demo after D1 and D2 | 0 |
| [S42369c35adcf](S42369c35adcf.md) | 2026-10-30T18:07:33.018Z | 4.7 | claude_code | Align demo reference lists with [withheld]'s typed entries | 0 |
| [S4d402d9f77ec](S4d402d9f77ec.md) | 2026-10-30T18:24:32.703Z | 78.9 | claude_code | D3: Appendix numbers from artifact and live runs | 29 |
| [Sfd509261b588](Sfd509261b588.md) | 2026-10-31T17:29:22.459Z | 16.5 | claude_code |  | 145 |
| [S608554912fb3](S608554912fb3.md) | 2026-10-31T17:29:38.358Z | 51.6 | claude_code |  | 0 |
| [S8e9170064d29](S8e9170064d29.md) | 2026-10-31T17:30:18.861Z | 6.7 | claude_code |  | 0 |
| [S7332ebfba1fc](S7332ebfba1fc.md) | 2026-10-31T18:22:13.162Z | 1.1 | claude_code |  | 2 |
