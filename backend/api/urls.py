from django.urls import path
from .views import *


urlpatterns = [
    path('note/', NoteCreateListView.as_view(), name="note-create-list-view"),
    path('note/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name="note-create-list-view")
   
]
