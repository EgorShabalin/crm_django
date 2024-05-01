# Generated by Django 4.2.10 on 2024-04-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0027_alter_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='course',
        ),
        migrations.AddField(
            model_name='contract',
            name='course',
            field=models.ManyToManyField(to='site_app.course', verbose_name='Course'),
        ),
    ]