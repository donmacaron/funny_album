Create Django management command scan_folder.

Behavior:
- read directory
- create albums from folders
- create media entries for files
- skip duplicates

Command example:
python manage.py scan_folder /media/import
