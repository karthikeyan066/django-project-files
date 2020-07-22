from django import forms
from .models import Register_form, breakfast_option, lunch_option,dinner_option
from bootstrap_datepicker_plus import DatePickerInput

class Customer(forms.Form):
	BREAKFAST =(('','choose....'),('1','Dosa'),('2','Pongal'),('3','Masal Puri'),('4','Vadai'),('5','Itly'))
	LUNCH =(('','choose....'),('1','Full_Meals'),('2','Veg_Biriyani'),('3','Chicken_Biriyani'),('4','Parotta'),('5','Noodles'))
	DINNER =(('','choose....'),('1','Dosa'),('2','Parotta'),('3','Chappathi'),('4','Naan'),('5','Fried_Rice'))

	customername = forms.CharField()
	date = forms.DateField()
	breakfast = forms.ChoiceField(choices = BREAKFAST)
	Lunch = forms.ChoiceField(choices = LUNCH)
	dinner = forms.ChoiceField(choices = DINNER)


class customerform(forms.ModelForm):
	BreakFast = forms.ModelChoiceField(queryset=breakfast_option.objects.all(), initial = 0)
	Lunch = forms.ModelChoiceField(queryset=lunch_option.objects.all(), initial = 0)
	Dinner = forms.ModelChoiceField(queryset=dinner_option.objects.all(),initial = 0)
	#Customer_Name = forms.CharField(error_messages = {'required': "This field is required"})
	#Date = forms.CharField(error_messages = {'required': "This field is required"})
	class Meta:
		model = Register_form
		fields = ['Customer_Name','Date','BreakFast','Lunch','Dinner']
		widgets={'Date': DatePickerInput()}
		#BreakFast ={'BreakFast': breakfast_option.objects.all()}
		#def __init__(self, *args, **kwargs):
			#super(customerform, self).__init__(*args, **kwargs)
			#self.fields['Customer_Name'].error_messages = {'required': 'This Field is Required'}

class breakfastform(forms.ModelForm):
	class Meta:
		model = breakfast_option
		fields = ['Breakfast_List']#,'Lunch_List']

class lunchform(forms.ModelForm):
	class Meta:
		model = lunch_option
		fields = ['Lunch_List']

class dinnerform(forms.ModelForm):
	class Meta:
		model = dinner_option
		fields = ['Dinner_List']







class fetchform(forms.Form):
	CustomerName = forms.CharField(max_length = 100)
	#Date = forms.DateField(widget=DatePickerInput())

				