# Generated by Django 2.0.6 on 2018-08-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180809_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('femail', 'Female'), ('not-specified', 'Not Specified')], max_length=80, null=True),
        ),
    ]