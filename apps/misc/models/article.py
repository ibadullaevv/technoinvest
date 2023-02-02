from django.db import models
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    title = models.CharField(max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     # return reverse('misc:items-by-category', args=[self.slug])
    #     return reverse('misc:category-detail', args=[self.slug])


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Article.Status.PUBLISHED)


class Article(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()
    category = TreeForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles')
    body = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('misc:item-detail', args=[self.slug])
