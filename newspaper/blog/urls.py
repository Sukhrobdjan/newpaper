from django.urls import path
from .views import HomePageView,NewsView

urlpatterns = [
    path( '', HomePageView.as_view(), name = 'home' ),
    path( 'about/', NewsView.as_view(), name = 'about' ),
]
