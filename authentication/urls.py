from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from authentication.views import *


urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace = 'restframework'))
]