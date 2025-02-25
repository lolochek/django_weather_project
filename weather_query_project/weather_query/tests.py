from unittest.mock import patch

from django.test import TestCase, Client
from django.urls import reverse

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

    @patch("requests.get")
    def test_search_weather_valid(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky'}]}

        response = self.client.post(reverse('search_weather'), {'city_name': 'Moscow'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Clear")
        self.assertContains(response, "Moscow")


    @patch("requests.get")
    def test_search_weather_invalid(self, mock_get):
        mock_get.return_value.status_code = 404

        response = self.client.post(reverse('search_weather'), {'city_name': 'aaaa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'City not found')

class QueryHistoryTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_query_history(self):
        Query.objects.create(city_name="Minsk",
                             weather_details={'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky'}]})

        response = self.client.get(reverse('get_query_history'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Clear")
        self.assertContains(response, "Minsk")
        self.assertEqual(len(response.context['history']), 1)