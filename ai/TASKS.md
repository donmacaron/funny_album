# Tasks — atomic todo list

## Setup
- init repo, virtualenv, basic Django project with Wagtail
- create single admin user scaffold

## Core models & admin
- implement Page (Wagtail Page or simple model)
- implement Album (nested)
- implement Media model + upload
- add thumbnails pipeline (Pillow + ffmpeg)

## Admin UX
- bulk upload view + import ZIP handler
- drag & drop ordering for media
- admin UI for menu management

## Folder scan
- management command `scan_folder /path/to/root`:
  - create Album nodes mirroring folders
  - create Media entries for files

## Permissions & sharing
- implement `ShareLink` (unique token, optional password, optional expiry)
- implement upload/download permissions for given user/email (simplified for single-user: create share links with upload rights)

## Frontend
- album listing, album fullscreen view
- multi-select + download (zip on-the-fly or pre-generated)
- simple theming (CSS variables + a small theme.json)

## Tests & docs
- unit tests for models, scan_folder, share links
- docs: README, deploy notes

## Deploy
- Dockerfiles: django + postgres + nginx + media volume
