# Project spec — Lightweight Photographer CMS

## Цель
Лёгкая однопользовательская CMS для фотографа/видеографа. Удобная админка для массового загрузка медиа, вложенных альбомов и публичного шаринга.

## Ключевые фичи
- Один пользователь (site owner / admin).
- Page: простые текстовые страницы (блог).
- Album: вложенные альбомы (self FK), атрибут public/private.
- Media: фото, видео, gif, аудио; thumbnails/previews.
- Bulk upload через админку (drag & drop / zip).
- Management command `scan_folder` — читает папку и создает альбомы/медиа.
- Create album from selected uploaded media.
- Permissions: возможность выдавать права на upload/download отдельным файлам или наборам.
- Меню: админ управляет пунктами меню (ссылка на Page или Album).
- Frontend: fullscreen gallery, multi-select download (если есть право).
- Минимальная theming (CSS variables).

## Технологии
- Backend: Django + Wagtail.
- Frontend: plain HTML/CSS/JS (progressive enhancement).
- DB: PostgreSQL (dev: sqlite ok).
- Media processing: Pillow + ffmpeg.

## Security & Constraints
- Validate file types & sizes.
- Store media paths safely; avoid traversal.
