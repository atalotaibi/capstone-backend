# Generated by Django 2.2 on 2019-04-18 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answered',
        ),
    ]