---
role: saturday-hours
title: Before-and-after comparison with a comparison group
kind: detour
summary: A second analysis that shows why a before/after change needs a comparison group, because other things also change over time.
time: 7 min
teaches: [verification, scoping-work]
needs: [clean-data]
---

After this step you will be able to ask for a before/after comparison and a comparison with unaffected sites, and you will know why the
second is more convincing than the first.

**Before you start:** cleaned data with dates, a site variable, and a change that happened at a known date ([Setup](setup:restore-a-starting-point)).

## Background

If an outcome changes after an intervention, other things may have changed too (season, staffing, policy). A **before/after** comparison
cannot separate these. Adding a **comparison group** that did not receive the change shows what would have happened anyway. The comparison of
the two changes is called **difference-in-differences**: the change at the intervention site minus the change at the comparison sites.

It still relies on an assumption (the sites would have moved in parallel without the change), so describe the result as consistent with an
effect, not as proof.

## General approach

```text
Using <clean data>, compare the share of visits that are <outcome> before and after <date> at <intervention site>. Then do the same for the
other sites combined. Report the counts, the change at each, and the difference between the changes with a 95% confidence interval. Use a
simple closed-form interval computed from the counts, with no bootstrap or simulation. Also show the monthly share for each site before the
change, as a table. State the assumptions.
```

Say how heavy a method you want. A comparison like this is four counts and one formula, and it should run in under a second. If a script runs
much longer than you expect, interrupt it and ask what it is doing ([Steering](concept:steering)).

<!-- example -->

## What to check

- The "before" and "after" periods and the comparison sites are what you intended.
- Counts for each cell of the before/after table are shown.
- The assumptions (parallel trends, no other change) are stated.

## Common problems

| Symptom | Cause | Fix |
|---|---|---|
| The script runs for minutes | The agent chose a resampling method, such as a bootstrap, or fitted several models | Interrupt it and ask for a closed-form interval. Visits from the same patient are not independent, so say so in the assumptions instead |
| Seasonal patterns drive the change | The periods cover different seasons | Compare the same months, or model month |
| Very few records before the change | The change happened early in the data | Say the baseline is thin and the estimate is imprecise |
