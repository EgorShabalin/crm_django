# Generated by Django 4.2.10 on 2024-04-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0039_alter_photo_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representative',
            name='student',
        ),
        migrations.AddField(
            model_name='representative',
            name='student',
            field=models.ManyToManyField(to='site_app.student', verbose_name='Student'),
        ),
    ]