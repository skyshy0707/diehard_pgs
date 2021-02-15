from django.db import models


from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.


class Input(models.Model):

	id = models.AutoField(primary_key=True)

	title = models.CharField(max_length=35)
	
	email = models.EmailField()
	
	file = models.FileField()
	
	
