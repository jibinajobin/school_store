# Generated by Django 4.2.9 on 2024-01-20 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0002_rename_user_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
