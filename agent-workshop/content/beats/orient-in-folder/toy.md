---
role: orient-in-folder
scenario: toy
starts_from: the data kit (`scenarios/toy/kit/`) copied into an empty folder
produces: nothing new; this step only reads
prompt: |
  What files are in this folder? Describe each in one line, and tell me which ones you could not read as plain text.
---

**What you should see.** About eleven files. The text-based ones (`clinic_notes.txt`, `data_dictionary.md`, the CSVs, and
`clinic_directory.html`) are readable directly. The agent should flag `clinic_targets.xlsx`, `pilot_protocol.docx`,
`patient_newsletter.pdf`, and `staffing.db` as needing a reader or conversion. The next steps deal with each.
