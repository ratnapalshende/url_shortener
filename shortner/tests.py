from django.test import TestCase
from django.urls import reverse
from .models import ShortenedURL

class URLShortenerTests(TestCase):

    def setUp(self):
        """Set up initial data for the tests"""
        self.url = "https://example.com"
        self.short_url = ShortenedURL.objects.create(url=self.url)
        self.short_code = self.short_url.shortCode

    def test_create_short_url(self):
        data = {"url": "https://example.com"}
        response = self.client.post(reverse('create_short_url'), data, content_type="application/json")
        self.assertEqual(response.status_code, 201)  # Expecting 201 Created response


    def test_retrieve_short_url(self):
        """Test retrieving the original URL using the short code"""
        response = self.client.get(reverse('retrieve', kwargs={'short_code': self.short_code}))
        self.assertEqual(response.status_code, 200)  # Should return 200 OK
        self.assertEqual(response.data['url'], self.url)

    def test_update_short_url(self):
        new_url = "https://newexample.com"
        response = self.client.put(
            reverse('retrieve', kwargs={'short_code': self.short_code}),
            {"url": new_url}, content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)  # Expecting 200 OK
        self.assertEqual(response.data['url'], new_url)


    def test_delete_short_url(self):
        """Test deleting a shortened URL"""
        response = self.client.delete(reverse('retrieve', kwargs={'short_code': self.short_code}))
        self.assertEqual(response.status_code, 204)  # Expecting 204 No Content
        # Check if the record is actually deleted
        with self.assertRaises(ShortenedURL.DoesNotExist):
            ShortenedURL.objects.get(shortCode=self.short_code)
