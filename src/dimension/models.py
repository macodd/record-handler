from django.db import models

from patient.models import Patient


class Dimension(models.Model):
    patient = models.OneToOneField(to=Patient, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    created_at = models.DateField(auto_now_add=True)

