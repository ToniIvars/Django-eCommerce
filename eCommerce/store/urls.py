from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('view-profile/<str:profile>', views.view_profile, name='view_profile')
]