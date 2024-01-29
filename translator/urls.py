from django.urls import path
from translator.views import home, translate_ajax, source_code

urlpatterns = [
    path('', home, name='home'),
    path('translate/', translate_ajax, name='translate_ajax'),
    path('code/', source_code, name='source_code'),
]