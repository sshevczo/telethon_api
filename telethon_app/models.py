from django.db import models

# Create your models here.
class TelethonClient(models.Model):
    phone_number = models.CharField(max_length=50)
    api_id = models.CharField(max_length=50)
    api_hash = models.CharField(max_length=50)
    session_name = models.CharField(max_length=50)
    