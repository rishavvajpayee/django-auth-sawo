from django.db import models

class ConfigModel(models.Model):
    api_key = models.CharField(max_length=200, unique=True)
    identifier = models.CharField(max_length=200)
    choices =[("email","Email")]