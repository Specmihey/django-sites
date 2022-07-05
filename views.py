from django.urls import path, re_path, include
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('<slug:dir_cat_slug>/<slug:dir_slug>/', Get_Direction_Item.as_view(), name='direction'), # Направления
    path('<slug:dir_cat_slug>/', cosmetology_by_sections.as_view(), name='directions_of_cosmetology'), # Разделы направлений
    path('', directions_of_cosmetology.as_view(), name='directions_of_cosmetology'), #Все разделы направлений
]
