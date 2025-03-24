from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .utility import haversine
from .utils import point_in_polygon 
from .models import Property
from .serializers import PropertySerializer

class PropertyListView(APIView):
    def get(self, request):
        
        # Get bounding box coordinates from query parameters
        min_lat = request.query_params.get('min_lat')
        min_lng = request.query_params.get('min_lng')
        max_lat = request.query_params.get('max_lat')
        max_lng = request.query_params.get('max_lng')

        # Validate query parameters
        if not all([min_lat, min_lng, max_lat, max_lng]):
            return Response(
                {"error": "All bounding box parameters (min_lat, min_lng, max_lat, max_lng) are required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            min_lat = float(min_lat)
            min_lng = float(min_lng)
            max_lat = float(max_lat)
            max_lng = float(max_lng)
        except ValueError:
            return Response(
                {"error": "Bounding box parameters must be valid numbers."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Filter properties within the bounding box
        properties = Property.objects.filter(
            latitude__gte = min_lat,
            latitude__lte = max_lat,
            longitude__gte = min_lng,
            longitude__lte = max_lng
        )
        print("properties", properties)

        # Serialize the queryset
        serializer = PropertySerializer(properties, many=True)
        print(serializer.data)

        # Return the serialized data
        response = {
            "status": 200,
            "success" : True,
            "message": "Properties within the specified bounding box",
            "properties": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    

class PorpertyCircleView(APIView):
    def get(self, request):
        # Get circle center coordinates and radius from query parameters
        center_lat = request.query_params.get('center_lat')
        center_lng = request.query_params.get('center_lng')
        radius = request.query_params.get('radius')
        
        
        # Validate query parameters
        if not all([center_lat, center_lng, radius]):
            return Response(
                {"error": "All circle parameters (center_lat, center_lng, radius) are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        
        try:
            center_lat = float(center_lat)
            center_lng = float(center_lng)
            radius = float(radius)
            
            radius_km = radius / 1000
            
        except ValueError:
            return Response(
                {"error": "Circle parameters must be valid numbers."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        print(center_lat, center_lng, radius)
        
        # Filter properties within the circle 
        properties = []
        for property in Property.objects.all():
            distance = haversine(center_lat, center_lng, property.latitude, property.longitude)
            print(center_lat, center_lng, property.latitude, property.longitude)
            if distance <= radius_km:
                properties.append(property)
                

        # Serializr the queryset
        serializer =  PropertySerializer(properties, many=True)
        
        # return the serializer data
        response = {
            "status": 200,
            "success" : True,
            "message": "Properties within the specified circle",
            "properties": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    

class PropertyPolygonView(APIView):
    def post(self, request):
        # Get polygon vertices from request body
        vertices = request.data.get('vertices')

        print("vertices", vertices)

        # Validate query parameters
        if not vertices or len(vertices) < 3:
            return Response(
                {"error": "A polygon must have at least 3 vertices."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Filter properties within the polygon
        properties = []
        for property in Property.objects.all():
            point = (property.latitude, property.longitude)
            if point_in_polygon(point, vertices):
                properties.append(property)

        # Serialize the queryset
        serializer = PropertySerializer(properties, many=True)

        # Return the serialized data
        response = {
            "status": 200,
            "success": True,
            "message": "Properties within the specified polygon",
            "properties": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)
    
    
# fronted view
def map_view(request):
    return render(request, 'properties/index.html')