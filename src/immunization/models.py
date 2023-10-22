from django.db import models

from patient.models import Patient


# Immunizations are One to One. These are specific to the patient
class Immunization(models.Model):
    patient = models.OneToOneField(to=Patient, on_delete=models.CASCADE)
    vaccine = models.CharField(max_length=128, null=False)
    location = models.CharField(max_length=256)
    next_dose = models.DateField()
    created_at = models.DateField(auto_now_add=True)
