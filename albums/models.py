from django.db import models


class Album(models.Model):
    """
    Album model with nested album structure support.
    
    Allows albums to have parent-child relationships for creating
    hierarchical/folder-like structures.
    """
    
    title = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        
    def __str__(self):
        return self.title
    
    @property
    def path(self):
        """Return the hierarchical path of this album."""
        parts = []
        current = self
        while hasattr(current, 'parent') and current.parent:
            if hasattr(current, 'title'):
                parts.append(current.title)
            current = current.parent
        
        # Reverse since we collected from bottom to top
        return '/'.join(reversed(parts)) if parts else str(self.id)
