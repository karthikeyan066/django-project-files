from django.urls import path
from . import views
 
urlpatterns =[
	path('index',views.index),
	path('customerentry',views.customerentry),
	path('fetchentry',views.fetchentry),
	path('dinnerentry',views.dinnerentry),
	path('bfentry',views.bfentry),
	path('luentry',views.luentry),
	path('trial',views.trial),

]