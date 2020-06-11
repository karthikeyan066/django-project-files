from django import forms

class Customer(forms.Form):
	"""docstring for ClassName"""
	customername = forms.CharField()
	date = forms.DateField()
	breakfast = forms.CharField(choices=[(''), ('Dosa'), ('Pongal'), ('Puri'), ('Vada'), ('Appam')])
	Lunch = forms.CharField(choices=[(''), ('Full Meals'), ('Veg_Biriyani'), ('Chicken_Biriyani'), ('Noodles'), ('Pulav')])
	dinner = forms.CharField(choices=[(''), ('Parotta'), ('Chappathi'), ('Dosa'), ('Fried_rice'), ('chilly_parotta')])
	