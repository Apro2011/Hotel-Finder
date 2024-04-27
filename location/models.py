from django.db import models
from django.contrib.gis.db import models  # GeoDjango Models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    street_1 = models.CharField(max_length=255)
    street_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    location = models.PointField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Hotel")
        verbose_name_plural = _("Hotels")

    def __str__(self) -> str:
        return f"{self.street_1}, {self.city}, {self.state}, {self.country}"
