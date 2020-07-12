from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

app_name = __package__
urlpatterns = [
	# path('login', views.login, name='login'),
	# path('register', views.register, name='register'),
	# path('logout', views.logout, name='logout'),

	# # reset users' password
	# path('password-reset', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html', email_template_name='account/emails/_password_reset_email.html', success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),
	# path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
	# path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html', success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),
	# path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
	
	# path('profile', views.profile, name='profile'),
	# path('', views.index, name='index')
]