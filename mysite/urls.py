from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

app_name = __package__

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
	path('', include('daira.urls')),
    path('', include('sokna.urls')),
    path('', include('pages.urls')),
]

# urlpatterns += i18n_patterns(
#     prefix_default_language=True
# )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)