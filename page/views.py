from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Customer, customerform, fetchform, breakfastform, lunchform, dinnerform
from .models import Register_form, breakfast_option, lunch_option, dinner_option
from django.db.models import Q
from django.contrib import messages
# Create your views here.
def index(request):
	return render(request,'add/index.html')


def customerentry(request):
	if request.method == 'POST':
		form = customerform(request.POST)
		if form.is_valid():
			temp = form.cleaned_data.get("Customer_Name")
			print(temp)
			form.save()
			messages.success(request, 'Data has been Successfully updated')
		else:
			messages.success(request,'Enter correct value')
			
			

	form = customerform()
	return render(request,'add/model.html', {'form' : form})


all_data = "NULL"
def fetchentry(request):
	#all_data = Register_form.objects.all()
	if request.method == "POST":
		global all_data
		fetch_name = request.POST["Customer Name"]
		fetch_date = request.POST["Date"]
		if fetch_name == "" and fetch_date == "":
			all_data = Register_form.objects.all()
		elif fetch_name != "" and fetch_date != "":
			all_data = Register_form.objects.filter(Q(Customer_Name = fetch_name) & Q(Date = fetch_date))
		elif fetch_date == "":
			all_data = Register_form.objects.filter(Customer_Name = fetch_name)
		else:
			all_data = Register_form.objects.filter(Date = fetch_date)


	return render(request,'add/fetchentry.html',{'all': all_data})




def bfentry(request):
	option = breakfast_option.objects.all()
	if request.method == 'POST':
		form = breakfastform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Data has been Successfully updated')
		else:
			messages.success(request,'Enter correct value')
	form = breakfastform()
	return render(request,'add/foodentry.html',{'breakfast' : form,'option': option})	
def luentry(request):
	data = lunch_option.objects.all()
	if request.method =='POST':
		value = lunchform(request.POST)
		if value.is_valid():
			value.save()
			messages.success(request, 'Data has been Successfully updated')
		else:
			messages.success(request,'Enter correct value')
	value = lunchform()		
	return render(request,'add/lunch.html',{'value' : value, 'data' : data})

def dinnerentry(request):
	all_value = dinner_option.objects.all()
	if request.method == 'POST':
		data = dinnerform(request.POST)
		if data.is_valid():
			data.save()
			messages.success(request, 'Data has been Successfully updated')
		else:
			messages.success(request,'Enter correct value')
	data = dinnerform()
	return render(request,'add/dinner.html', {'data' : data, 'allvalue' : all_value})

def trial(request):
	return render(request,'add/trial.html')