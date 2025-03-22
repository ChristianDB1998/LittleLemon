from django.urls import path
from .views import *

#include url patterns here.
urlpatterns = [
    path('menu-items/', MenuItemsView.as_view(), name='menuitems'),
    path('menu-item/<int:pk>', SingleMenuItemView.as_view(), name='single-menuitem'),
]