from django.db import models
from django import forms

from inputData.models import Input

from django.contrib.postgres.fields import JSONField


# Create your models here.

class Results(models.Model):

	
	generator = models.OneToOneField(Input, on_delete = models.CASCADE, primary_key = True)
	
	pvalues = JSONField()
	