# Generated by Django 4.2.10 on 2024-04-29 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0034_student_end_date_student_form_of_study_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
