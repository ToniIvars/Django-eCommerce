from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('view-profile/<str:profile>', views.view_profile, name='view_profile')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)