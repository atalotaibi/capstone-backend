# Generated by Django 2.2 on 2019-04-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20190427_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='major',
            field=models.CharField(choices=[('COMPUTER SCIENCE', 'Computer Science'), ('COMMUNICATIONS', 'Communications'), ('POLITICAL SCIENCE', 'Political Science'), ('BUSINESS', 'Business'), ('ECONOMICS', 'Economics'), ('PSYCHOLIGY', 'Psychology'), ('MATH', 'Math'), ('BIOLOGY', 'Biology'), ('INFORMATION SYSTEM TECHNOLOGY', 'Information System Technology'), ('CYBER SECURITY', 'Cyber Security'), ('HUMAN RESUORCE ', 'Humen Resuorce '), ('ACCOUNTING', 'Accounting'), ('ELECTRICAL ENGINEERING', 'Electrical Engineering'), ('MECHANICAL ENGINEERING', 'Mechanical Engineering'), ('BIOMEDICAL ENGINEERING', 'Biomedical Engineering')], max_length=24),
        ),
    ]