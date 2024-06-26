# Generated by Django 4.2.10 on 2024-03-19 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0005_student_personal_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='residence_permit_end_date',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Residence Permit End Date'),
        ),
        migrations.AddField(
            model_name='student',
            name='residence_permit_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Residence Permit ID'),
        ),
    ]
