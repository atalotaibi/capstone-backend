# Generated by Django 2.2 on 2019-04-27 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20190425_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major',
            name='name',
        ),
        migrations.AddField(
            model_name='major',
            name='major',
            field=models.CharField(choices=[('COMPUTER SCIENCE', 'Computer Science'), ('COMMUNICATIONS', 'Communications'), ('POLITICAL SCIENCE', 'Political Science'), ('BUSINESS', 'Business'), ('ECONOMICS', 'Economics'), ('PSYCHOLIGY', 'Psychology'), ('MATH', 'Math'), ('BIOLOGY', 'Biology'), ('INFORMATION SYSTEM TECHNOLOGY', 'Information System Technology'), ('CYBER SECURITY', 'Cyber Security'), ('HUMAN RESUORCE ', 'Humen Resuorce '), ('ACCOUNTING', 'Accounting'), ('ELECTRICAL ENGINEERING', 'Electrical Engineering'), ('MECHANICAL ENGINEERING', 'Mechanical Engineering'), ('BIOMEDICAL ENGINEERING', 'Biomedical Engineering')], default=1, max_length=23),
        ),
    ]