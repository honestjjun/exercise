from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.title
