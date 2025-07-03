from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer

class PersonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
