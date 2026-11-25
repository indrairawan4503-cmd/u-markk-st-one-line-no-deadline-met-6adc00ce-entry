# NOTES — One Line, No Deadline Met (variant B)

Concept (assigned): "The deadline and I have an open relationship." — the deadline saw other people.

## Iterations (one concept, v1–v8)

- v1 (94 chars / 96 bytes): The deadline and I have an open relationship — it saw other people, and I saw other deadlines.
  Symmetric wordplay, but "other deadlines" is abstract — the punch doesn't land on the missed deadline itself.
- v2 (93 chars / 93 bytes): The deadline and I have an open relationship. It saw other people first, so I stopped trying.
  "Stopped trying" is a shrug, not a punch; the turn fizzles.
- v3 (94 chars / 96 bytes): The deadline and I have an open relationship — it started seeing other people, so I let it go.
  "Let it go" is too gentle; reads like acceptance, not an excuse.
- v4 (86 chars / 88 bytes): Me and the deadline had an open relationship — it saw other people, I saw the weekend.
  "I saw the weekend" is a concrete scene, but it confesses slacking outright — less of a joke, more of an admission.
- v5 (97 chars / 97 bytes): The deadline and I have an open relationship: it saw other people, I saw three seasons of a show.
  Concrete and relatable, but the show-binge angle is well-worn and the punch is predictable.
- v6 (90 chars / 90 bytes): The deadline and I agreed on an open relationship, but it was the one seeing other people.
  Clean reversal, but it ends on the setup rather than a punch — no payoff after the turn.
- v7 (113 chars / 115 bytes): The deadline and I have an open relationship — it saw other people, and honestly, they were better at meeting it.
  WINNER. The punch ("they were better at meeting it") lands on the missed deadline itself: the others met it, I didn't. Self-deprecating, spoken voice ("and honestly"), single sentence, fresh angle.
- v8 (103 chars / 103 bytes): The deadline and I have an open relationship. It saw other people, so I figured it wasn't that into me.
  Good breakup-voice punch, but "wasn't that into me" is about the relationship, not the deadline — v7 ties the joke back to meeting the deadline, which is the excuse itself.

## Final line (v7)

The deadline and I have an open relationship — it saw other people, and honestly, they were better at meeting it.

- 113 chars, 115 bytes (UTF-8, em dash = 3 bytes), no trailing newline. Gate: 1–200 chars. ✓
- Why it won: one concrete scene (open relationship) + one surprising turn (the other people were better at meeting the deadline). It IS the excuse, it reads cleanly aloud as one sentence, the punch lands at the end, and "and honestly" makes it sound like something a person would actually say when cornered.

## Validation

- main.py run twice; /output/entry.txt byte-identical both runs: sha256 d8f75b4ca4dc00fef1e38a80d622433b54dffcc188dc2d7883af248f64f07a99 (run 1 and run 2).
- Read-only grader simulation: copy to /tmp, chmod -R a-w, run main.py — exit 0, /output/entry.txt sha256 d8f75b4ca4dc00fef1e38a80d622433b54dffcc188dc2d7883af248f64f07a99. ✓
- entry.txt byte-identical to main.py output.
- LICENSE line 1: `SPDX-License-Identifier: MIT` + full MIT text.
- .makefun/owner.json: exactly {"wallet": "FT1ect39XkeTprHy44WyUFprgHZbEUxAvQkWKspfiuPH"}.
- README.md: official template adapted — 3 live make.fun badges for this slug, owner indrairawan4503-cmd, repo u-markk-st-one-line-no-deadline-met-6adc00ce-entry, referral footer ref 8dxq9bq0.
- git: local commit only. No GitHub repo, no push, no bundle, no submit (coordinator's job).
