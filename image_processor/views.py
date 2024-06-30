from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from image_processor.serializers import *
from image_processor.models import *
from image_processor.utils import *



# Create your views here.
class TestViewset(ModelViewSet):
    serializer_class = TestSerializer
    # parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']
    filterset_fields = ['user']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        return Test.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Save the object
        self.perform_create(serializer)
        
        # Access the created object and its ID
        test = serializer.instance
        
        # Call the other function with the user_id

        results = extract_chemical_colors(test.image)
        self.create_results(results, test)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def create_results(self, results, test):

        for chemical in results:
            result_obj = Result.objects.create(test=test, 
                                chemical=chemical['chemical'], 
                                red=chemical['rgb'][0],
                                green=chemical['rgb'][1],
                                blue=chemical['rgb'][2])
