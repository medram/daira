from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = __package__

urlpatterns = [
    # path('sokna/', views.create_sokna, name='create_sokna'),
    # path('sokna/<int:id>/', views.sokna_detail, name='sokna_detail')
    path('sokna/', views.SoknaList.as_view()),
    path('sokna/<int:pk>/', views.SoknaDetail.as_view()),
    path('administrative-attache/', views.Mol7akaList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
