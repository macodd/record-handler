from django.db import models

from patient.models import Patient


# Allergies can be used by Many to Many
# Various Patients can have the same allergy
class Allergy(models.Model):
    patient = models.OneToOneField(to=Patient, on_delete=models.CASCADE)
    name = models.TextField(max_length=128)
    created_at = models.DateField(auto_now_add=True)
