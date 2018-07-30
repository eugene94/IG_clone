# Generated by Django 2.0.6 on 2018-07-30 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180714_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('femail', 'Female'), ('not-specified', 'Not Specified'), ('male', 'Male')], max_length=80, null=True),
        ),
    ]
