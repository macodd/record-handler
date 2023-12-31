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
            name='Dimension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('weight', models.DecimalField(decimal_places=1, max_digits=5, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
            ],
        ),
    ]
