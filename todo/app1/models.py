from django.db import models

# Create your models here.
class Textstore(models.Model):
    textmodel = models.TextField()
    isdelete = models.BooleanField(null=True,default=False)