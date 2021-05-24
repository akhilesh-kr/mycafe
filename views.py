from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

def index(request):
	return render(request,'mycafe/index.html',{'name':'akhilesh'})
def reservations(request):
	if request.method=='POST':
		name=request.POST['Name']
		username=request.POST['username']
		email=request.POST['E-Mail']
		password=request.POST['pwd']
		date=request.POST['Date']
		time=request.POST['Time']
		no_of_people=request.POST['no_of_people']

		user=User.objects.create_user(username=username,password=password,email=email)
		user.save()
		print('user created')
		
	else:
		return render(request,'mycafe/reservations.html',{'name':'Akhilesh'})
def aboutus(request):
	return render(request,'mycafe/aboutus.html',{'name':'Akhilesh'})
def contact(request):
	return render(request,'mycafe/contact.html',{'name':'akhilesh'})
def menu(request):
	return render(request,'mycafe/menu.html',{'name':'name'})