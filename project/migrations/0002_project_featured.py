# Generated by Django 2.0.7 on 2018-11-10 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
