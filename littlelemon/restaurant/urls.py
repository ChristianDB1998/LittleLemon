from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

#include url patterns here.
urlpatterns = [
    path('menu-items/', MenuItemsView.as_view(), name='menuitems'),
    path('menu-item/<int:pk>', SingleMenuItemView.as_view(), name='single-menuitem'),
    path('api-token-auth/', obtain_auth_token),
]