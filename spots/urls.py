from django.urls import path
from .views import CarSpotCreateView

urlpatterns = [
    path('upload/', CarSpotCreateView.as_view(), name='carspot-upload'),
]
