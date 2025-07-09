from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from . serializers import UserSerializer, ProfileSerializer, RegistrationSerializer
from . models import Profile

class RegistrationView(APIView):
    def post(self,request):
        try:
            serializers = RegistrationSerializer(data = request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":str(e)})
        