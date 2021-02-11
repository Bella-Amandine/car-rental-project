from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'register'),
    path('', views.index, name = 'index'),
    path('post/vehicle/', views.post_vehicle, name = 'new_vehicle'),
    path('vehicle/<vehicle_id>', views.single_vehicle, name = 'vehicle')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)