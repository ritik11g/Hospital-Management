# Generated by Django 3.1 on 2020-11-23 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_patient_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempappointments',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
