from rest_framework.test import APITestCase
from rest_framework import status
from .models import Note

class NoteTests(APITestCase):
    
    def test_create_note(self):
        response = self.client.post('/api/notes/create/', {'title': 'Test Note', 'body': 'This is a test note.'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 1)
        self.assertEqual(Note.objects.get().title, 'Test Note')

    def test_get_note_by_id(self):
        note = Note.objects.create(title='Test Note', body='This is a test note.')
        response = self.client.get(f'/api/notes/{note.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Note')

    def test_query_notes_by_title(self):
        Note.objects.create(title='Test Note 1', body='Body 1')
        Note.objects.create(title='Test Note 2', body='Body 2')
        response = self.client.get('/api/notes/', {'title': 'Test Note'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_note(self):
        note = Note.objects.create(title='Old Title', body='Old body.')
        response = self.client.put(f'/api/notes/{note.id}/update/', {'title': 'New Title', 'body': 'New body.'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        note.refresh_from_db()
        self.assertEqual(note.title, 'New Title')
