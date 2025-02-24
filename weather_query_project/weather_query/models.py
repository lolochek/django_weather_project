from django.db import models

# Create your models here.

class Query(models.Model):
    city_name = models.TextField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    weather_details = models.JSONField()

