# Generated by Django 4.1.13 on 2024-02-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
