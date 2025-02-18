from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from Music.models import Artist


class ArtistAPITestCase(APITestCase):

    def setUp(self):
        self.artist_url = reverse('artist-list')
        self.valid_payload = {
            "name": "Test Artist",
            "bio": "A famous test artist",
            "country": "Testland"
        }

    def test_create_artist(self):
        response = self.client.post(self.artist_url, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 1)

        artist = Artist.objects.first()
        self.assertEqual(artist.name, self.valid_payload["name"])
        self.assertEqual(artist.bio, self.valid_payload["bio"])
        self.assertEqual(artist.country, self.valid_payload["country"])
