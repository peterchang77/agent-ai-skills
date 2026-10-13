---
role: build-cohort
title: Build a study cohort with a flow table
kind: full
summary: Translate formal study eligibility criteria into a reproducible cohort dataset, accompanied by an attrition flow diagram reconciling excluded populations.
time: 8 min
teaches: [verification, tools, inputs]
needs: [clean-data]
---

Empirical research requires defining an unambiguous study population. In this exercise, you direct the agent to translate written clinical eligibility criteria into a reproducible cohort dataset (`out/cohort.csv`) alongside a formal cohort attrition diagram (`out/cohort_flow.md`) tracking sample sizes across each selection rule.

**Before you start:** Cleaned data and a written study protocol or cohort specification ([Setup](setup:restore-a-starting-point)).

## Background

In observational study design, an unambiguous cohort definition specifies four distinct parameters:

- **Target population:** Broad demographic or clinical eligibility criteria (e.g., adults receiving care at designated clinic sites).
- **Index event:** The precise anchor timestamp that initiates follow-up for each individual (e.g., the first qualifying encounter within the study window).
- **Exposure classification:** The operational definition distinguishing exposed individuals from controls.
- **Outcome observation window:** The defined temporal interval following the index event during which endpoints are ascertained.

Ambiguity in eligibility criteria is a primary source of silent bias. When rules reside in study protocols or memos, require the agent to read the document and **quote the exact eligibility sentences** before writing any code ([Inputs](concept:inputs)).

An **attrition flow table** (or PRISMA/STROBE cohort flow diagram) documents sample counts retained and excluded at each stage. Any discrepancy between step counts indicates unintended record drops ([Verification](concept:verification)).

## General methodology

Instruct the agent to audit protocol definitions, quote the source rules, and generate an executable cohort creation script:

```text
Read <protocol file>. Quote the exact eligibility criteria, index event definition, exposure criteria, and outcome observation window.
Then write an executable script (<scripts/build_cohort.py>) applying these rules to <clean data>.
Generate a cohort dataset (<out/cohort.csv>) with strictly one row per individual, and an attrition flow table (<out/cohort_flow.md>) reporting counts remaining after each selection rule.
Classify an individual as exposed if <exposure condition>; categorize all remaining eligible individuals as unexposed controls so no eligible subjects are dropped.
Explicitly document any areas where protocol phrasing required interpretation.
```

Requiring the agent to highlight interpretive assumptions ensures domain choices remain visible for researcher confirmation.

<!-- example -->

## Verification criteria

- **Protocol alignment:** The quoted eligibility rules match the protocol source text verbatim.
- **Unit of observation integrity:** The final cohort dataset contains strictly one record per patient ID.
- **Monotonic sample reduction:** Each row in the attrition flow table is less than or equal to the prior count, and the final flow count matches `out/cohort.csv` exactly.
- **Transparent assumptions:** The agent explicitly documents edge-case assumptions (e.g., handling ties in same-day visits) for your review.

## Common pitfalls

| Symptom | Underlying cause | Resolution |
|---|---|---|
| Multiple rows per patient ID | Index event logic failed to restrict records to the initial qualifying encounter | Instruct the agent to group records by patient ID and slice the earliest qualifying event |
| Unexposed comparison group is unexpectedly small | Records lacking explicit exposure logs were coded as null and dropped | Explicitly define the control group as all eligible cohort members who do not meet exposure criteria |
| Sample size diverges from historical benchmarks | Discordant temporal window boundary interpretations (e.g., `< 30` vs. `<= 30` days) | Reconcile window boundary expressions against protocol definitions |
