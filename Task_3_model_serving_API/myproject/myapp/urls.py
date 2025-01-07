from django.urls import path
from .views import predict_view, home_view  # Ensure these views exist

urlpatterns = [
    path('', home_view, name='home'),  # Home page view
    path('predict/', predict_view, name='predict'),  # Prediction view
]