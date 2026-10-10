---
role: review-with-second-agent
scenario: toy
starts_from: the `analyzed` checkpoint (open a **new** session in it)
produces: nothing saved (ask for the review as `out/review.md` if you want to keep it)
prompt: |
  You are reviewing someone else's analysis. Read pilot_protocol.docx, scripts/analyze_pilot.py and out/pilot_results.md. Check the
  cohort rules and the outcome definition in the script against the protocol, line by line. List errors, questionable assumptions, and
  anything in the results not supported by the data. Do not change any files. Rank the issues and give the evidence for each.
---

**Files used:** `pilot_protocol.docx`, `scripts/analyze_pilot.py`, `out/pilot_results.md`.

**What a good review finds.** For this analysis the reference solution is correct, so a careful reviewer should mostly confirm the
definitions and then raise **limitations**, such as:

- Call assignment was not random, so residual confounding is possible beyond age.
- The outcome counts any measured HbA1c in the window, regardless of which visit type produced it.
- Patients with no follow-up at all are counted as "not rechecked", which is the intended outcome but depends on the clinic being the only place they would be tested.
- The interval is wide (the lower bound is near 1), so the estimate is imprecise.

**A better test: plant an error.** To see the reviewer work, change one thing in a copy of the script, such as counting a call *attempt* as
exposure (the exposed group becomes 103 instead of 92) or changing the window to 14 to 90 days, then ask a fresh session to review it. A good
reviewer should find the mismatch with the protocol. That also shows why the exposure and window definitions were quoted in the cohort step.

**What a review cannot do.** It cannot tell you whether "reached by a call" is the right exposure for your question. That judgement is yours.
