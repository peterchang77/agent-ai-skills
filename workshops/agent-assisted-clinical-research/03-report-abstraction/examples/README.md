# Illustrative abstraction cases

These fabricated examples are for understanding the output contract and validator. They are not source data and not few-shot prompt content unless the instructor explicitly chooses to use them.

## Valid temporal evidence

**Current impression:** `Mild diffuse pulmonary edema has improved. Small bilateral pleural effusions are unchanged.`

A valid result can label pulmonary edema `improved` with the exact quote `pulmonary edema has improved`, and pleural effusion `stable` with `pleural effusions are unchanged`, provided the comparison is otherwise aligned and certain.

## Invalid: bare negative is not resolution

**Current impression:** `No pleural effusion. Mild bibasilar atelectasis.`

Do not label pleural effusion `resolved` from `No pleural effusion` alone. There is no explicit temporal disappearance. Use an abstention/non-target state or mask it as appropriate.

## Invalid: isolated non-opacity finding

**Current impression:** `Minimal left basilar atelectasis, unchanged.`

Do not label `lung_opacity` solely from isolated atelectasis. The validator should mask a purported lung-opacity target with the appropriate reason unless other explicit opacity language supports it.

## Invalid: uncertainty

**Current impression:** `Possible mild pulmonary edema, not significantly changed.`

The statement may be clinically meaningful but is not a certain target under this workshop contract. It must be masked rather than forced into `stable`.

## Invalid: evidence from wrong source

If the claimed evidence quote appears only in the prior impression, it cannot support a usable change label. The current impression is the required evidence source.
