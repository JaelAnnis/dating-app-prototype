# Generated by Django 4.0.4 on 2022-05-31 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UnMask', '0003_rename_users_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
