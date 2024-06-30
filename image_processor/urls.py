from django.urls import path 
from rest_framework.routers import DefaultRouter 
from image_processor.views import *

router = DefaultRouter()
router.register(r'tests', TestViewset, basename='test')

urlpatterns = router.urls