from django.db import models

class Services(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    content = models.TextField(blank=True, verbose_name="content")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name="photo")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="create time")
    time_update = models.DateTimeField(auto_now=True, verbose_name="update time")
    is_published = models.BooleanField(default=True, verbose_name="is published?")
    
    class Meta():
        verbose_name = "Service"
        verbose_name_plural = "Services"