from django.urls import path
from . import views


app_name = __package__

handler404 = 'pages.views.error_404'
handler403 = 'pages.views.error_403'
handler500 = 'pages.views.error_500'

urlpatterns = [
	path('<slug:slug>', views.index)	
]