# Generated by Django 2.0.6 on 2018-08-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20180806_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('femail', 'Female'), ('male', 'Male'), ('not-specified', 'Not Specified')], max_length=80, null=True),
        ),
    ]
