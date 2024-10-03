from django.urls import path, include

from .views import StudentRegisterAPIView, TeacherRegisterAPIView

urlpatterns = [
    path("sign-up/student/", StudentRegisterAPIView.as_view()),
    path("sign-up/teacher/", TeacherRegisterAPIView.as_view()),
]