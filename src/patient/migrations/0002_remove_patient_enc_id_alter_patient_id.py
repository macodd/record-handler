# Generated by Django 4.2.5 on 2023-10-09 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='enc_id',
        ),
        migrations.AlterField(
            model_name='patient',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
