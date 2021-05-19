from django.urls import path, include
from rest_framework import routers

from student_course.views import CourseViewSet


router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
