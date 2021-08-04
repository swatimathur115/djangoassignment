from django.db import models
#from django.contrib import admin
#import datetime
#from autoslug import AutoSlugField
from django_extensions.db.fields import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
	category_name = models.CharField(max_length=200)
	slug = AutoSlugField(populate_from=['category_name'])
	def __str__(self):
		return self.category_name

class Tag(models.Model):
	name = models.CharField(max_length=200, unique=True)
	slug = AutoSlugField(populate_from=['name'])
	def __str__(self):
		return self.name

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField(null=True,blank=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	category = models.ForeignKey(Category,null=True, blank=True,on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag,related_name='tags')
	image= models.ImageField(null=True,blank=True)
		
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class CustomUser(AbstractUser):
	profileimage = models.ImageField()

class Comment(models.Model):
	post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
	name=models.CharField(max_length=200, unique=True)
	comment=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	parent = models.ForeignKey('self', null=True,on_delete=models.CASCADE, related_name='replies')