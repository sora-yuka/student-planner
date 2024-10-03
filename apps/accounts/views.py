from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import get_user_model
from .serializers import UserRegisterSerializer
from .tasks import send_verification_link


User = get_user_model()


class StudentRegisterAPIView(APIView):
    def post(self, request: Request) -> Response:
        try:
            serializer = UserRegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
        except IntegrityError:
            return Response(data={
                "MESSAGE": "Something went wrong while registering student.",
                "STATUS": status.HTTP_400_BAD_REQUEST,
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user.is_student = True
        user.save()
        
        send_verification_link.delay(user.email, user.verification_code)
        
        return Response(data={
            "MESSAGE": "We send verificaiton link to your email. Please follow the link, and activate account.",
            "STATUS": status.HTTP_201_CREATED,
        }, status=status.HTTP_201_CREATED)


class TeacherRegisterAPIView(APIView):
    def post(self, request: Request) -> Response:
        try:
            serializer = UserRegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
        except IntegrityError:
            return Response(data={
                "MESSAGE": "Something went wrong while registering student.",
                "STATUS": status.HTTP_400_BAD_REQUEST,
            }, status=status.HTTP_400_BAD_REQUEST)
            
        user.is_teacher = True
        user.save()
        
        send_verification_link.delay(user.email, user.verification_code)
        
        return Response(data={
            "MESSAGE": "We send verificaiton link to your email. Please follow the link, and activate account.",
            "STATUS": status.HTTP_201_CREATED,
        }, status=status.HTTP_201_CREATED)