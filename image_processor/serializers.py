from rest_framework.serializers import ModelSerializer, ImageField
from authentication.serializers import CustomUserSerializer
from action_serializer import ModelActionSerializer
from image_processor.models import *

class ResultSerializer(ModelSerializer):

    class Meta:
        model = Result
        exclude = ['test']

class TestSerializer(ModelActionSerializer):
    results = ResultSerializer(many=True, required=False)
    # user = CustomUserSerializer()

    class Meta:
        model = Test
        fields = ['user', 'image', 'created_at', 'results']
        read_only_fields = ['created_at', 'results']
        action_fields = {
            'list': {
                'fields' : ('id', 'image', 'created_at', 'user')
            },
            'retrieve': {
                'fields' : ('id', 'image', 'created_at', 'user', 'results')
            }

        }


