from django.urls import path
from . import views
from .views import home, landing

urlpatterns = [

    path('',views.landing,name='landing-page'),
    path('home/',views.home,name='home'),
]