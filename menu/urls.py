from django.urls import path

from menu.views import base_menu

app_name = 'menu'

urlpatterns = [
    path('', base_menu, name='home'),
    path('menu/<slug:category>/', base_menu, name='category'),
]
