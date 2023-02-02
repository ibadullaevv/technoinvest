from django.db import models
from solo.models import SingletonModel


class AboutCompany(SingletonModel):
    title = models.CharField(max_length=50)
    text = models.TextField()
    image1 = models.ImageField(upload_to='company')
    image2 = models.ImageField(upload_to='company')
    image3 = models.ImageField(upload_to='company')

    def __str__(self):
        return self.title


class OurService(SingletonModel):
    title = models.CharField(max_length=20)
    title1 = models.CharField(max_length=20)
    text1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=20)
    text2 = models.CharField(max_length=100)
    title3 = models.CharField(max_length=20)
    text3 = models.CharField(max_length=100)

    def __str__(self):
        return self.title

