# Generated by Django 4.2.10 on 2024-03-07 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='representative',
            old_name='child',
            new_name='student',
        ),
    ]
