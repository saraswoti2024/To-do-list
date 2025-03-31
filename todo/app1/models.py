from django.db import models
from django.utils import timezone

# Create your models here.
class Textstore(models.Model):
    textmodel = models.TextField()
    isdelete = models.BooleanField(null=True,default=False)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)