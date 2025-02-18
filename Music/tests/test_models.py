from django.test import TestCase
from django.db.utils import IntegrityError
from Music.models import Artist


class ArtistModelTest(TestCase):

    def test_create_artist(self):
        artist = Artist.objects.create(
            name="Иван Иванов",
            bio="Известный художник",
            country="Россия"
        )
        self.assertEqual(artist.name, "Иван Иванов")
        self.assertEqual(artist.bio, "Известный художник")
        self.assertEqual(artist.country, "Россия")
        self.assertIsNotNone(artist.created_at)

    def test_unique_name(self):
        Artist.objects.create(name="Уникальный артист")
        with self.assertRaises(IntegrityError):
            Artist.objects.create(name="Уникальный артист")
