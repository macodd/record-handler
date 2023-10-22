from django.db import models
from django.conf import settings

from patient.models import Patient


class Medic(models.Model):
    ruc = models.IntegerField(primary_key=True)  # must have RUC
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    specialty = models.CharField(max_length=256)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    patients = models.ManyToManyField(to=Patient, through="Membership")


class Membership(models.Model):
    patient = models.ForeignKey(to=Patient, on_delete=models.PROTECT)
    medic = models.ForeignKey(to=Medic, on_delete=models.PROTECT)
    date_linked = models.DateField(auto_now_add=True)
    date_unlinked = models.DateField(null=True)
    active = models.BooleanField(default=False)
