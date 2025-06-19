from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Shot, Practice
from .serializers import ShotSerializer, PracticeSerializer, UserSerializer

class ShotListCreateView(generics.ListCreateAPIView):
    queryset = Shot.objects.all()
    serializer_class = ShotSerializer
    permission_classes = [permissions.AllowAny]

class PracticeListCreateView(generics.ListCreateAPIView):
    serializer_class = PracticeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Practice.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

@api_view(['GET', 'POST'])
@permission_classes([permissions.AllowAny])
def shot_list_create(request):
    if request.method == 'GET':
        shots = Shot.objects.all()
        serializer = ShotSerializer(shots, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ShotSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([permissions.AllowAny])
def shot_detail(request, pk):
    try:
        shot = Shot.objects.get(pk=pk)
    except Shot.DoesNotExist:
        return Response({'error': 'Shot not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShotSerializer(shot)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = ShotSerializer(shot, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        shot.delete()
        return Response({'message': 'Shot deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])  
def practice_list_create(request):
    if request.method == 'GET':
        practices = Practice.objects.filter(user=request.user)
        serializer = PracticeSerializer(practices, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PracticeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])  
def practice_detail(request, pk):
    try:
        practice = Practice.objects.get(pk=pk, user=request.user)
    except Practice.DoesNotExist:
        return Response({'error': 'Practice log not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PracticeSerializer(practice)
        return Response(serializer.data)
    elif request.method in ['PUT', 'PATCH']:
        serializer = PracticeSerializer(practice, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        practice.delete()
        return Response({'message': 'Practice log deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        return Response({
            "message": "Login successful",
            "user_id": user.id,
            "username": user.username
        })
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_profile_view(request):
    user = request.user
    total_practices = Practice.objects.filter(user=user).count()
    shots_count = Shot.objects.count()
   
    from django.db.models import Count
    favorite_shot_data = Practice.objects.filter(user=user).values('shot__name').annotate(
        count=Count('shot')).order_by('-count').first()
    
    favorite_shot = favorite_shot_data['shot__name'] if favorite_shot_data else "None"
    
    profile_data = {
        'name': user.get_full_name() or user.username,
        'email': user.email,
        'favoriteShot': favorite_shot,
        'totalShots': shots_count,
        'shotsCompleted': total_practices,
        'streak': 0, 
    }
    
    return Response([profile_data])  