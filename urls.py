from django.urls import path
from . import views

urlpatterns=[
	path('home', views.index , name='name'),
	path('reservations',views.reservations,name='name'),
	path('aboutus',views.aboutus,name='name'),
	path('contact',views.contact,name='name'),
	path('menu',views.menu,name='name'),
]