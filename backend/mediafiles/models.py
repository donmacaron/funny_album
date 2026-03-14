from django.db import models


class Media(models.Model):
    MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
        ('gif', 'GIF'),
        ('audio', 'Audio'),
    ]

    file = models.ImageField(upload_to='uploads/media/', blank=True, null=True)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.media_type} - {self.album.name}"
