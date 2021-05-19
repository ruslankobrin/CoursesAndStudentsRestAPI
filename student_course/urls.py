from django.urls import path, include
from rest_framework import routers

from student_course.views import CourseViewSet, CourseParticipantViewSet

router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'course_patisipants', CourseParticipantViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
