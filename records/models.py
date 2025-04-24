from django.db import models

class MedicalTerm(models.Model):
    term = models.CharField(max_length=100)
    definition = models.TextField()
    domain = models.CharField(max_length=100)  # e.g., "Cardiology", "Hematology"

class MedicalRange(models.Model):
    term = models.ForeignKey(MedicalTerm, on_delete=models.CASCADE)
    min_value = models.FloatField()
    max_value = models.FloatField()


class UploadedReport(models.Model):
    filename = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    extracted_text = models.TextField()
    parsed_data = models.JSONField()
    pdf_file = models.FileField(
        upload_to='uploaded_reports/',
        null=True,     
        blank=True     
    )

