from __future__ import unicode_literals
from django.db import models

LOCATION = (
	('Mombasa', 'Mombasa'),
	('Nairobi', 'Nairobi'),
	('Kisumu', 'Kisumu'),
	)

CATEGORY = (
	('Kienyeji', 'Kienyeji'),
	('Kenbrew', 'Kenbrew'),
	('Layers', 'Layers'),
	('Broilers', 'Broilers'),
	)

class Post(models.Model):
	title = models.CharField(max_length=100, blank=True, default='')
	description = models.TextField(blank=True, default='')
	price = models.FloatField()
	category = models.CharField(max_length=100, choices=CATEGORY, default='')
	location = models.CharField(max_length=100, choices=LOCATION, default='')
	image1 = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')
	image2 = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')
	image3 = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg')
	owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)

def save(self, *args, **kwargs):
	Super(Post, self).save(*args, **kwargs)