from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import StudentView, TeacherView,StudentList


router=DefaultRouter()
router.register('studentapi',StudentView, basename="student")
router.register('teachertapi',TeacherView, basename="teacher")


urlpatterns = [
    path("", include(router.urls)),
    path('admin/', admin.site.urls),
    path("stulist", StudentList.as_view(), name='studentlist')
]
