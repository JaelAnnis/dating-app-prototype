# Generated by Django 4.0.4 on 2022-05-31 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UnMask', '0004_alter_profile_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='profile',
            name='interested_men',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interested_women',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
