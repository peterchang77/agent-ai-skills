# Context: CheXpert Plus data discovery

The workshop uses the Stanford AIMI CheXpert Plus release, version `v1.0`, available through Redivis in the sandbox example as dataset `AIMI.chexpert_plus:5yyj`. The source project's metadata table is `df_chexpert_plus_240401`; the release also exposes label and image/file tables. Treat these names as deployment-specific starting points: inspect the accessible workspace rather than assuming every listed table is present or small.

The full release is multi-terabyte scale. Discovery must precede export. A small metadata trial may use fields such as `deid_patient_id`, `path_to_image`, `findings`, `impression`, and `split`, but the agent must obtain actual column names from the endpoint.

The original sandbox used the Redivis Python client and device authentication. The workshop cloud image may instead mount prepared data. Follow the actual workspace landing page and do not recreate credentials or embed them in code.

Later exercises need a small, documented metadata export, not a full image collection. The download utility must make the table, columns, destination, and optional row limit explicit. It must refuse to overwrite an existing file.

Relevant safety rules are in [`../shared/data-and-llm-safety.md`](../shared/data-and-llm-safety.md) and the environment contract is in [`../shared/workspace-contract.md`](../shared/workspace-contract.md).
