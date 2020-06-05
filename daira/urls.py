from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = __package__

urlpatterns = [
	path('', views.home, name='home'),
]