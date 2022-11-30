from django.db import models

from .utils import generate_random_string


class ShortenedURL(models.Model):
    
    url = models.TextField()
    slug = models.CharField(max_length=10, db_index=True, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        pass
    
    def __str__(self):
        return self.slug
    
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            slug_exists = True
            while (slug_exists):
                slug = generate_random_string()
                slug_exists = ShortenedURL.objects.filter(slug=slug).exists()
            
            self.slug = slug
            
        return super().save(*args, **kwargs)
    