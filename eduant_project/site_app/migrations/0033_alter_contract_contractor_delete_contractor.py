# Generated by Django 4.2.10 on 2024-04-29 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0032_representative_contractor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='contractor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='site_app.representative', verbose_name='Contractor'),
        ),
        migrations.DeleteModel(
            name='Contractor',
        ),
    ]
