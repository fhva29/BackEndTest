from django.urls import path
from .views import get_dividends

urlpatterns = [
    path("<symbol>/<year>/", get_dividends, name="dividends"),
]