# Generated by Django 4.2.5 on 2023-09-25 08:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('epokabootcamp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
