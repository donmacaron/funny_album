# Deploy notes
- Use Docker Compose: django + postgres + nginx + volume for /media.
- Serve static via nginx, protect private albums (signed URLs or proxy through Django).
- Use cloud storage for media in prod (S3 / Cloudflare R2).
