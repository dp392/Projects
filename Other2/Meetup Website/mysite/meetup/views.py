from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import TemplateView

import datetime
from .models import User, Activities

def user(request):
	if request.method == 'POST':
		userId = request.POST['userId']
		userName = request.POST['userName']
		userFirstName = request.POST['userFirstName']
		userLastName = request.POST['userLastName']
		userEmail = request.POST['userEmail']
		userGender = request.POST['userGender']
	try:
		user = User.objects.get(userId=int(userId))
		user.userName = userName
		user.userFirstName = userFirstName
		user.userLastName = userLastName
		user.userEmail = userEmail
		user.userGender = userGender
		user.userLastOnline = datetime.datetime.now()
		user.save()
	except:
		user = User(userId = userId, userFirstName = userFirstName, userLastName = userLastName, userName = userName, userEmail = userEmail, userGender = userGender, userLastOnline = datetime.datetime.now())
		user.save()
	return HttpResponse(user)

def home(request):
	user = User.objects.get(pk=1)
	context = {'user': user}
	return render(request, 'meetup/home.html', context)

def matches(request, id):
	user = User.objects.get(pk=id)
	context = {'user': user}
	return render(request, 'meetup/matches.html', context)

def addActivities(request):
	if request.method == 'POST':
		activityName = request.POST['activityName']
	user = User.objects.get(pk=1)
	try:
		newActivity = Activities.objects.create(activitiesUserId=user, activitiesName=activityName)
		newActivity.save()
		print newActivity
		return HttpResponse(user)
	except Exception as e:
		print e
		return HttpResponse(status=400)