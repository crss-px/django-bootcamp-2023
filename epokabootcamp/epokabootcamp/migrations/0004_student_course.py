# Generated by Django 4.2.1 on 2023-09-28 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epokabootcamp', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='epokabootcamp.course'),
            preserve_default=False,
        ),
    ]
