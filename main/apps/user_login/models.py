
# # Inside models.py
#   from __future__ import unicode_literals
#   from django.db import models
#   # Create your models here.
#   class Blog(models.Model):
#       name = models.CharField(max_length=255)
#       desc = models.TextField()
#       created_at = models.DateTimeField(auto_now_add = True)
#       updated_at = models.DateTimeField(auto_now = True)
#   class Comment(models.Model):
#       comment = models.CharField(max_length=255)
#       created_at = models.DateTimeField(auto_now_add = True)
#       updated_at = models.DateTimeField(auto_now = True)
#       # Notice the association made with ForeignKey for a one-to-many relationship
#       # There can be many comments to one blog
#       blog = models.ForeignKey(Blog, related_name = "comments")
#   class Admin(models.Model):
#       first_name = models.CharField(max_length=255)
#       last_name = models.CharField(max_length=255)
#       email = models.CharField(max_length=255)
#       blogs = models.ManyToManyField(Blog, related_name = "admins")
#       created_at = models.DateTimeField(auto_now_add = True)
#       updated_at = models.DateTimeField(auto_now = True)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email_address = models.CharField(max_length=255)
	age = models.IntegerField()
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __repr__(self):
		return "<User Object name: {} {} email: {} age: {} created: {} updated:{}".format(self.first_name, self.last_name, self.email_address, self.age, self.create_at, self.updated_at)
