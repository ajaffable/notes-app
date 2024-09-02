from django.urls import path
from .views import NoteCreateView, NoteRetrieveView, NoteUpdateView, NoteListView

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='note-list'),
    path('notes/<int:pk>/', NoteRetrieveView.as_view(), name='note-detail'),
    path('notes/create/', NoteCreateView.as_view(), name='note-create'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note-update'),
]
