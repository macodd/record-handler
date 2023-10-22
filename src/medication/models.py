from django.db import models

from .choices import Frequency, Dose
from medic.models import Medic
from patient.models import Patient


# These are One to One with Patients
class Medication(models.Model):
    patient = models.OneToOneField(to=Patient, on_delete=models.CASCADE)
    prescribed_by = models.OneToOneField(to=Medic, on_delete=models.CASCADE)  # 'dr <medication_name>'
    name = models.CharField(max_length=256)  # 'aspirin'
    brand = models.CharField(null=True, max_length=256)  # 'finalin'
    quantity = models.PositiveSmallIntegerField(default=0)  # '2'
    dose = models.PositiveSmallIntegerField(null=True, choices=Dose.choices)  # 'pills'
    every = models.PositiveSmallIntegerField(default=1)  # 'every 4'
    frequency = models.PositiveSmallIntegerField(null=True, choices=Frequency.choices)  # 'hours'
    notes = models.TextField(max_length=512)  # 'no more than 6 per day'
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_dose(self):
        return Dose(self.dose).name

    def get_frequency(self):
        return Frequency(self.frequency).name
