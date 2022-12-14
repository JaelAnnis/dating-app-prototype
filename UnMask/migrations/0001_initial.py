# Generated by Django 4.0.4 on 2022-05-10 02:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('birthdate', models.DateTimeField(null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='')),
                ('latitude', models.CharField(max_length=3, null=True)),
                ('longitude', models.CharField(max_length=3, null=True)),
                ('description', models.CharField(max_length=700, null=True)),
                ('min_age', models.IntegerField(max_length=3, null=True)),
                ('max_age', models.IntegerField(max_length=3, null=True)),
                ('min_distance', models.IntegerField(max_length=3, null=True)),
                ('interested_men', models.BooleanField(null=True)),
                ('interested_women', models.BooleanField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
