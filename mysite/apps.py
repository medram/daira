from django.contrib.admin.apps import AdminConfig

# to create a custom adminSite
class MyAdminConfig(AdminConfig):
	default_site = 'mysite.admin.MyAdminSite'