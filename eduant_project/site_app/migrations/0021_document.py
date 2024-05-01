# Generated by Django 4.2.10 on 2024-04-18 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0020_internship'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_leaving_certificate', models.FileField(upload_to='', verbose_name='School leaving certificate')),
                ('passport', models.FileField(upload_to='', verbose_name='Passport')),
                ('form', models.FileField(upload_to='', verbose_name='Form')),
                ('application', models.FileField(upload_to='', verbose_name='Application')),
                ('photo', models.FileField(upload_to='', verbose_name='Photo')),
                ('birth_cert', models.FileField(upload_to='', verbose_name='Birth certificate')),
                ('exit_application', models.FileField(upload_to='', verbose_name='Exit application')),
                ('agreement_for_residence_permit', models.FileField(upload_to='', verbose_name='Agreement for residence permit')),
                ('medical_cert', models.FileField(upload_to='', verbose_name='Medical certificate')),
                ('hiv_cert', models.FileField(upload_to='', verbose_name='HIV certificate')),
                ('description', models.FileField(upload_to='', verbose_name='Description')),
                ('other', models.FileField(upload_to='', verbose_name='Other')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated time')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.student', verbose_name='Student')),
            ],
        ),
    ]