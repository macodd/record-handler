from django.db import models

from .choices import BloodType


class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    dob = models.DateField(null=False)
    blood_type = models.PositiveSmallIntegerField(
        default=BloodType.UNKNOWN.value,
        choices=BloodType.choices)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_blood_type(self):
        return BloodType(self.blood_type).name

    def set_blood_type(self, blood_type: BloodType, commit: bool = False):
        self.blood_type = blood_type.value
        if commit:
            self.save()
