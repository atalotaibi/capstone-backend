# Generated by Django 2.2 on 2019-04-21 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_user_major'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Major',
        ),
    ]
