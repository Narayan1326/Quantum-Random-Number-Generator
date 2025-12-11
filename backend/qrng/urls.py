from django.urls import path

from .views import QuantumRandomAPIView


urlpatterns = [
    path("random/", QuantumRandomAPIView.as_view(), name="qrng-random"),
]

