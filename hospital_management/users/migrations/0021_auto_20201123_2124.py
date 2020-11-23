# Generated by Django 3.1 on 2020-11-23 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_remove_doctor_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='users.departments'),
        ),
        migrations.AlterField(
            model_name='departments',
            name='department',
            field=models.CharField(default='Dept.', max_length=50),
        ),
    ]
