from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import CarSpot


class CarSpotListView(ListView):
    model = CarSpot
    template_name = "spots/carspot_list.html"
    context_object_name = "carspots"


class CarSpotCreateView(CreateView):
    model = CarSpot
    fields = ["brand", "model", "year", "image", "description", "latitude", "longitude"]
    template_name = "spots/carspot_form.html"
    success_url = reverse_lazy("carspot-upload")
