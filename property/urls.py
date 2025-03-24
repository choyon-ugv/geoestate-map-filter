from django.urls import path
from .views import PropertyListView, PorpertyCircleView, PropertyPolygonView, map_view

urlpatterns = [
    path('properties/rectangle/', PropertyListView.as_view(), name='property-rectangle'),
    path('properties/circle/', PorpertyCircleView.as_view(), name='property-circle'),
    path('properties/polygon/', PropertyPolygonView.as_view(), name='property-polygon'),
    path('map/', map_view, name='map-view'),  # Add this line
]