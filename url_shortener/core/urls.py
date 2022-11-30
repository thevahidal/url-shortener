from django.urls import path

from .views import ShortenURLView, RedirectView

urlpatterns = [
    path('shorten/', ShortenURLView.as_view()),
    path('u/<str:slug>/', RedirectView.as_view()),
]