# Generated by Django 5.0.5 on 2024-05-06 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_carmodel_created_at_carmodel_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='body_type',
        ),
        migrations.RemoveField(
            model_name='carmodel',
            name='engine',
        ),
    ]
