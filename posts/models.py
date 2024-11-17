from django.db import models

# Create your models here.

class post_model(models.Model):
    author_name = models.CharField(max_length=70)
    psot_title = models.TextField(max_length=150)
    discriptions =models.TimeField(max_length=200)