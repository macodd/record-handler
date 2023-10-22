from django.db.models import IntegerChoices


class BloodType(IntegerChoices):
    UNKNOWN = 0
    O_POSITIVE = 1
    O_NEGATIVE = 2
    A_POSITIVE = 3
    A_NEGATIVE = 4
    B_POSITIVE = 5
    B_NEGATIVE = 6
    AB_POSITIVE = 7
    AB_NEGATIVE = 8
