from django.test import TestCase
from django.urls import reverse


class CarSpotUploadTests(TestCase):
    def test_upload_page_get(self):
        response = self.client.get(reverse("carspot-upload"))
        self.assertEqual(response.status_code, 200)
