from django.db import models


class CarSpot(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="spots/")
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        year = f" {self.year}" if self.year else ""
        return f"{self.brand} {self.model}{year}"
