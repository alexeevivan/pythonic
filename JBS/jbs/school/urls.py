from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('', Index_View.as_view(), name='index'),
    path('course', Course_View.as_view(), name='course'),
    path('course/bartender', Bartender_Course_View.as_view(), name='bartender'),
]