# Generated by Django 4.2.5 on 2023-10-10 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient', '0002_remove_patient_enc_id_alter_patient_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
