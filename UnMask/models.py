from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  first_name = models.CharField(max_length=50, null=True)
  last_name = models.CharField(max_length=50, null=True)
  birthdate = models.CharField( max_length=3, null=True)
  phone = models.CharField(max_length=10, null=True)
  email = models.CharField(max_length=100, null=True)
  profile_pic = models.ImageField(null=True, blank=True)
  latitude = models.CharField(null=True, max_length=6)
  longitude = models.CharField(null=True, max_length=6)
  description = models.CharField(max_length=700, null=True)
  min_age = models.IntegerField(max_length=3, null=True)
  max_age = models.IntegerField(max_length=3, null=True)
  min_distance = models.IntegerField(max_length=3, null=True)
  interested_men = models.BooleanField(default=False)
  interested_women = models.BooleanField(default=False)
  #date_created = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return self.first_name


class Matches(models.Model):
  profile1 =  models.ForeignKey(Profile, related_name='profile1', on_delete=models.CASCADE)
  profile2 =  models.ForeignKey(Profile, related_name='profile2', on_delete=models.CASCADE)
  profile1_match = models.BooleanField(default=False)
  profile2_match = models.BooleanField(default=False)
 
  def __str__(self):
    return "%s and %s" % ( self.profile1, self.profile2 )




