from django.urls import path
from .views import *

urlpatterns = [
    path('',Projectpage.as_view(), name='home'),
    path('video/',Videopage.as_view(), name='video'),
    path('kenyan/',Kenyanpage.as_view(), name='kenyan'),
    path('signup/',Signup.as_view(), name='signup'),

]