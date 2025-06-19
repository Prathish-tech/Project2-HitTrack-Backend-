from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Shot, Practice

class ShotSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Shot
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            else:
                return f"http://localhost:8000{obj.image.url}"
        return None
    
class PracticeSerializer(serializers.ModelSerializer):
    shot = ShotSerializer(read_only=True)
    shot_id = serializers.PrimaryKeyRelatedField(queryset=Shot.objects.all(), source='shot', write_only=True)
    
    class Meta:
        model = Practice
        fields = ['id', 'user', 'shot', 'shot_id']
        read_only_fields = ['user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

