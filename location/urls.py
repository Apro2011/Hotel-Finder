from django.urls import path
from location.views import ListCreateGenericViews, HotelUpdateRetrieveView

urlpatterns = [
    path("hotels", ListCreateGenericViews.as_view()),
    path(
        "hotels/<str:pk>",
        HotelUpdateRetrieveView.as_view(),
    ),
]
