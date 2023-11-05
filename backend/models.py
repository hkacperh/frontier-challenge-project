from django.db import models

# Create your models here.
class Network(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)  # 'No risk of failure', 'Risk of failure', 'Risk confirmed'