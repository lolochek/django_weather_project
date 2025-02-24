from django.test import TestCase, Client
from .models import Query
from .forms import CityNameForm

# Create your tests here.

class ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.q1 = Query.objects.create(city_name="Minsk",
                                  weather_details={'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky'}]})
    def test_query_content(self):
        self.assertEqual(self.q1.city_name, "Minsk")
        self.assertIsNotNone(self.q1.timestamp)
        self.assertEqual(self.q1.weather_details['weather'][0]['main'], 'Clear')
        self.assertEqual(self.q1.weather_details['weather'][0]['description'], 'clear sky')

class FormTest(TestCase):
    def test_validation(self):
        f1 = CityNameForm(data={"city_name": "Minsk"})
        self.assertTrue(f1.is_valid())
        f2 = CityNameForm(data={"city_name": ""})
        self.assertFalse(f2.is_valid())

class WeatherSearchTest(TestCase):
    def setUp(self):
        self.client = Client()

