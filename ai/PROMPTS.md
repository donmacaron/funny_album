# Prompts — ready-to-use prompts for Qwen 3.5 9B

## General dev assistant
You are a senior Django/Wagtail developer. Output only the files to change and their content, prefixed by ">>> path/to/file". Prefer small, single-purpose patches.

## Create Album model (example)
Task: implement Album model with nested albums (self FK), boolean public, optional cover (Media).
Constraints: single admin user, simple API endpoints for listing.
Reply format: show `models.py` patch, migration command, and a minimal unit test file.

## Bulk upload
Task: implement admin bulk upload endpoint that accepts zip or multi-file drag-drop. Outline backend steps and a small JS snippet for frontend upload progress.

## scan_folder
Task: implement management command `scan_folder` with safe path checks and optional dry-run mode. Provide tests.
