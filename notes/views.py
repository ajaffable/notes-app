from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from drf_spectacular.utils import extend_schema,OpenApiParameter,OpenApiTypes


class NoteCreateView(generics.CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @extend_schema(
        summary="Create a new note",
        request=NoteSerializer,
        responses={201: NoteSerializer},
        description="Create a new note with the given title and content."
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

class NoteRetrieveView(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @extend_schema(
        summary="Retrieve a specific note",
        responses={200: NoteSerializer},
        description="Retrieve the details of a specific note by its ID."
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NoteUpdateView(generics.UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @extend_schema(
        summary="Update a specific note",
        request=NoteSerializer,
        responses={200: NoteSerializer},
        description="Update the details of a specific note by its ID."
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class NoteListView(generics.ListAPIView):
    serializer_class = NoteSerializer

    @extend_schema(
        summary="List all notes",
        request=None,
        responses={200: NoteSerializer(many=True)},
        description="Retrieve a list of all notes. Optionally filter by title substring using the 'title' query parameter.",
        parameters=[
            OpenApiParameter(name='title', type=OpenApiTypes.STR, description='Filter notes by title substring', required=False)
        ]
    )
    def get(self, request, *args, **kwargs):        
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        title_substring = self.request.query_params.get('title', None)
        if title_substring:
            return Note.objects.filter(title__icontains=title_substring)
        return Note.objects.all()
