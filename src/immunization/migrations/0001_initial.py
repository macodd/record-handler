# Generated by Django 4.2.5 on 2023-10-09 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Immunization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=256)),
                ('next_dose', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
