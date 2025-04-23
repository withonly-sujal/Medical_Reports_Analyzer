from django.db import models

class MedicalTerm(models.Model):
    term = models.CharField(max_length=100)
    definition = models.TextField()
    domain = models.CharField(max_length=100)  # e.g., "Cardiology", "Hematology"

class MedicalRange(models.Model):
    term = models.ForeignKey(MedicalTerm, on_delete=models.CASCADE)
    min_value = models.FloatField()
    max_value = models.FloatField()
