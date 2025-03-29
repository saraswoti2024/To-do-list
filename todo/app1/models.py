from django.db import models

# Create your models here.
class Textstore(models.Model):
    textmodel = models.TextField()
    checks = models.BooleanField(default=False)