from django.test import TestCase
from .models import Query

# Create your tests here.

class ModelTesting(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.q1 = Query.objects.create(city_name="Minsk",
                                  weather_details={'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky'}]})
    def test_query_content(self):
        self.assertEqual(self.q1.city_name, "Minsk")
        self.assertIsNotNone(self.q1.timestamp)
        self.assertEqual(self.q1.weather_details['weather'][0]['main'], 'Clear')
        self.assertEqual(self.q1.weather_details['weather'][0]['description'], 'clear sky')