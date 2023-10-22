from django.db.models import IntegerChoices


class Frequency(IntegerChoices):
    HOURLY = 0
    DAILY = 1
    WEEKLY = 7
    BIWEEKLY = 14
    MONTHLY = 30
    ONCE = 365


class Dose(IntegerChoices):
    MG = 0
    ML = 1
    PILL = 2
    DROP = 3
    SHOT = 4
