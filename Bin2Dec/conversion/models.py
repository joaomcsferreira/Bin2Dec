from django.db import models

class Conversion(models.Model):
    num = models.CharField(max_length=8)
    convertion = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
