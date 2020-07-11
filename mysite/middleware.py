from django.conf import settings
from django.utils import translation

def LocaleAdminMiddleware(get_response):

	def middleware(request):
		if 'admin' in request.path:
			language = translation.get_language_from_request(request)
			translation.activate(settings.LANGUAGE_CODE)
			request.LANGUAGE_CODE = translation.get_language()
		
		response = get_response(request)
		
		translation.deactivate()
		
		return response
	return middleware