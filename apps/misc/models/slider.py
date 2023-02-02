from django.db import models
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Slider.Status.PUBLISHED)


class Slider(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()
    image = models.ImageField(upload_to='news')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
