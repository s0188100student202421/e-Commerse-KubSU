from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from ..models import User
from ..serializers import UserRegisterSerializer, UserProfileSerializer

def generate_jwt(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(hours=24),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = generate_jwt(user)
            return Response({'token': token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
            serializer = UserProfileSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, user_id):
        token = request.headers.get('Authorization', '').split(' ')[-1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            if payload['user_id'] != user_id:
                return Response(status=status.HTTP_403_FORBIDDEN)
            
            user = User.objects.get(id=user_id)
            serializer = UserProfileSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except (jwt.ExpiredSignatureError, jwt.DecodeError):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, user_id):
        token = request.headers.get('Authorization', '').split(' ')[-1]
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            if payload['user_id'] != user_id:
                return Response(status=status.HTTP_403_FORBIDDEN)
            
            User.objects.filter(id=user_id).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
        except (jwt.ExpiredSignatureError, jwt.DecodeError):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
