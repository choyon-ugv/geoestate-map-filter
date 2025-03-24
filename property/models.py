from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()  # Store latitude
    longitude = models.FloatField()  # Store longitude
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name