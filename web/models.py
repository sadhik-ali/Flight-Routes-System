from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.code


class Route(models.Model):
    parent = models.ForeignKey(Airport, related_name="routes", on_delete=models.CASCADE)
    child = models.ForeignKey(
        Airport, related_name="parent_routes", on_delete=models.CASCADE
    )
    position = models.CharField(max_length=10)  # Left / Right
    duration = models.IntegerField()  # in KM or time

    def __str__(self):
        return f"{self.parent} -> {self.child} ({self.duration})"
