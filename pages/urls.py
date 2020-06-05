from django.urls import path
from . import views

app_name = __package__

urlpatterns = [
	path('<slug:slug>', views.index)	
]