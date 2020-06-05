from django.urls import path

from . import views

app_name = __package__

urlpatterns = [
	path('sokna', views.register, name='register')
]