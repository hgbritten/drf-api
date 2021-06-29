from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Hike

# Create your tests here.
class HikeTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_hike = Hike.objects.create(
            author=testuser1,
            title="Emmons Route",
            body="Wonderful views up to the top of Mt. Rainier",
        )
        test_hike.save()

    def test_hike_content(self):
        hike = Hike.objects.get(id=1)
        actual_author = str(hike.author)
        actual_title = hike.title
        actual_body = hike.body

        expected_author = "testuser1"
        expected_title = "Emmons Route"
        expected_body = "Wonderful views up to the top of Mt. Rainier"

        self.assertEqual(actual_author, expected_author)
        self.assertEqual(actual_title, expected_title)
        self.assertEqual(actual_body, expected_body)
