# Generated by Django 4.2.10 on 2024-04-30 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0040_remove_representative_student_representative_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='representative',
            name='representative_type',
            field=models.CharField(blank=True, choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Representative', 'Representative')], max_length=255, null=True, verbose_name='Representative type'),
        ),
        migrations.AlterField(
            model_name='student',
            name='form_of_study',
            field=models.CharField(blank=True, choices=[('In Person', 'In Person'), ('Distance', 'Distance')], max_length=255, null=True, verbose_name='Form of study'),
        ),
    ]
