from django.shortcuts import render
from rest_framework import generics
from .models import NoteModel
from .serializers import NoteModelSerializer

class NoteCreateListView(generics.ListCreateAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer

class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteModelSerializer




