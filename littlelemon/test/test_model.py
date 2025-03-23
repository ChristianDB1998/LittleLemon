from django.test import TestCase
from restaurant.models import Menu
from datetime import datetime
from django.utils.timezone import make_aware


#Create test case for Menu Model
class MenuTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            name= "Freschante Expresso Specials", 
            no_of_guests=4, 
            bookingDate=make_aware(datetime(2025, 3, 25, 20, 25))
        )

    def test_get_item(self):
        self.assertEqual(self.menu.name, "Freschante Expresso Specials")
        self.assertEqual(self.menu.no_of_guests, 4)

    def test_string_representation(self):
        self.assertEqual(str(self.menu), "Freschante Expresso Specials")
    