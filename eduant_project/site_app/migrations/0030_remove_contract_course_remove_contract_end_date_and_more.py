# Generated by Django 4.2.10 on 2024-04-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0029_subject_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='course',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='form_of_study',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='pay_date',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='start_date',
        ),
        migrations.AddField(
            model_name='contract',
            name='final_settlement_date',
            field=models.DateField(blank=True, null=True, verbose_name='Final settlement date'),
        ),
    ]