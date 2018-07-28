from django.db import models
from django.utils import timezone
# Create your models here.

class Information(models.Model):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    facebook = models.URLField(max_length=50)
    twitter = models.URLField(max_length=50)
    pinterest = models.URLField(max_length=50)
    google = models.URLField(max_length=50)
    background = models.ImageField(upload_to='website_images')


class About(models.Model):
    title1 = models.CharField(null=True,blank=True,max_length=50)
    paragraph1 = models.TextField(null=True,blank=True)
    title2 = models.CharField(null=True,blank=True,max_length=50)
    paragraph2 = models.TextField(null=True,blank=True)
    title3 = models.CharField(null=True,blank=True,max_length=50)
    paragraph3 = models.TextField(null=True,blank=True)
    title4 = models.CharField(null=True,blank=True,max_length=50)
    paragraph4 = models.TextField(null=True,blank=True)

class Classes(models.Model):
    title1 = models.CharField(max_length=50)
    paragraph1 = models.TextField()
    MWF1 = models.CharField(max_length=20)
    TTHS1 = models.CharField(max_length=20)
    title2 = models.CharField(max_length=50)
    paragraph2 = models.TextField()
    MWF2 = models.CharField(max_length=20)
    TTHS2 = models.CharField(max_length=20)
    title3 = models.CharField(max_length=50)
    paragraph3 = models.TextField()
    MWF3 = models.CharField(max_length=20)
    TTHS3 = models.CharField(max_length=20)

class Instructors_Row(models.Model):
    name1 = models.CharField(max_length=20,null = True ,blank=True)
    image1 = models.ImageField(upload_to='instructors_images', null = True ,blank=True)
    name2 = models.CharField(max_length=20 ,null = True ,blank=True)
    image2 = models.ImageField(upload_to='instructors_images', null = True ,blank=True)

    


class Email(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    class Meta:
        default_permissions = ('change')

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts_images')
    date = models.DateField()
    paragraph = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Test(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    class Meta:
        default_permissions = ('add','change')