from django.contrib import admin

from .models import CarSpot


@admin.register(CarSpot)
class CarSpotAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year", "created_at")
