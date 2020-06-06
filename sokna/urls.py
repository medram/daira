from django.urls import path

from . import views

app_name = __package__

urlpatterns = [
	path('sokna', views.index, name='index'),
	path('sokna/follow', views.follow, name='follow'),
	path('sokna/register', views.register, name='register'),
	path('sokna/done/<int:id>', views.done, name='done')
]