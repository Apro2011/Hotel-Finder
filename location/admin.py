from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from location.models import Hotel


# Register your models here.
@admin.register(Hotel)
class HotelAdmin(LeafletGeoAdmin):
    list_display = ("id", "name", "location", "created_at", "updated_at")
