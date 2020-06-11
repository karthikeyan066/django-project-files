from django.db import models
#from .models import breakfast_option
# Create your models here.

class Register_form(models.Model):
	#BREAKFAST =(breakfast_option.object.all())
	#LUNCH =(('','choose....'),('Full_Meals', 'Full_Meals'),('Veg_Biriyani', 'Veg_Biriyani'),('Chicken_Biriyani', 'Chicken_Biriyani'),('Parotta', 'Parotta'),('Noodles', 'Noodles'))
	#DINNER =(('','choose....'),('Dosa','Dosa'),('Parotta', 'Parotta'),('Chappathi','Chappathi'),('Naan','Naan'),('Fried_Rice','Fried_Rice'))
	
	Customer_Name = models.CharField(max_length=100,blank=False)
	Date = models.DateField(blank=False)
	BreakFast = models.CharField(max_length=50, blank=True)
	Lunch = models.CharField(max_length=50,  blank=True)
	Dinner = models.CharField(max_length=50,  blank=True)
	def __str__(self):
		return self.Customer_Name
		
class breakfast_option(models.Model):
	Breakfast_List = models.CharField(max_length=50)
	#Lunch_List = models.CharField(max_length=50,default="", blank=True)
	def __str__(self):
		return self.Breakfast_List

class lunch_option(models.Model):
	Lunch_List = models.CharField(max_length=50)
	def __str__(self):
		return self.Lunch_List

class dinner_option(models.Model):
	Dinner_List = models.CharField(max_length=50)
	def __str__(self):
		return self.Dinner_List
