from django.conf.urls import url
from .views import get_Course 

urlpatterns = [
    url(r'^$', get_Course),
    
]