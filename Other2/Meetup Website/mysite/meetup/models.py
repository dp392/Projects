from django.db import models

# Create your models here.
class User(models.Model):
	userName = models.CharField(max_length=100)
	userFirstName = models.CharField(max_length=50)
	userLastName = models.CharField(max_length=50)
	userId = models.CharField(max_length=50, primary_key=True)
	userLastOnline = models.DateTimeField()
	userActivities = models.CharField(max_length=100)
	userEmail = models.EmailField(max_length=50)
	userGender = models.EmailField(max_length=50)

class Activities(models.Model):
	activitiesName = models.CharField(max_length=45)
	activitiesUserId = models.ForeignKey(User)