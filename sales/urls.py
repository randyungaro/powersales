from django.urls import path
from . import views  # Import views from the sales app

urlpatterns = [
    path('', views.daily_sales, name='daily_sales'),
]