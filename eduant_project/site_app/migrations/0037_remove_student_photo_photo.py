# Generated by Django 4.2.10 on 2024-04-29 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0036_student_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='photo',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='photo', to='site_app.student', verbose_name='Photo')),
            ],
        ),
    ]
