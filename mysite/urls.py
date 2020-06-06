from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = __package__

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('daira.urls')),
    path('', include('sokna.urls')),
    path('', include('pages.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)