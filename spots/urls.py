from django.urls import path
from .views import CarSpotCreateView, CarSpotListView

urlpatterns = [
    path('', CarSpotListView.as_view(), name='carspot-list'),
    path('upload/', CarSpotCreateView.as_view(), name='carspot-upload'),
]
