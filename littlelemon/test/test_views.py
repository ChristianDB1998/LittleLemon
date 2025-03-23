from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
from django.utils.timezone import make_aware
from datetime import datetime


# class MenuViewTest(TestCase):
#     def setUp(self):
#         self.menu = Menu.objects.create(
#             name= "Freschante Expresso Specials", 
#             no_of_guests=4, 
#             bookingDate=make_aware(datetime(2025, 3, 25, 20, 25))
#         )

#     def test_getall(self):


class MenuViewTest(TestCase):
    def setUp(self):
        """Set up test data and API client before each test"""
        self.client = APIClient()  # Initialize the API test client

        # Create multiple test instances of Menu
        self.menu1 = Menu.objects.create(
            name="Freschante Expresso Specials",
            no_of_guests=4,
            bookingDate=make_aware(datetime(2025, 3, 25, 20, 25))
        )

        self.menu2 = Menu.objects.create(
            name="Caramel Latte Delight",
            no_of_guests=2,
            bookingDate=make_aware(datetime(2025, 4, 1, 15, 30))
        )

    def test_getall(self):
        """Test retrieving all Menu objects and validating serialized data"""
        response = self.client.get('/restaurant/menu-items/')  # URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)  #Expecting 200 OK

        # Serialize expected data
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Compare API response with serialized data
        self.assertEqual(response.data, serializer.data)