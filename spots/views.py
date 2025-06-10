from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import CarSpot


class CarSpotCreateView(CreateView):
    model = CarSpot
    fields = ["brand", "model", "year", "image", "description", "latitude", "longitude"]
    template_name = "spots/carspot_form.html"
    success_url = reverse_lazy("carspot-upload")
