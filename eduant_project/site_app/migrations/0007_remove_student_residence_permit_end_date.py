# Generated by Django 4.2.10 on 2024-03-19 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0006_student_residence_permit_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='residence_permit_end_date',
        ),
    ]
