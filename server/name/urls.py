from django.urls import path
from .views import PersonListCreateAPIView

urlpatterns = [
    path('people/', PersonListCreateAPIView.as_view()),
]
