# Generated by Django 3.2.9 on 2021-11-18 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'get_latest_by': 'modified'},
        ),
    ]