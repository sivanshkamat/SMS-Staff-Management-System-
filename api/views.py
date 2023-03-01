
#This us gonna be merged by mod1 to the master
#This mod is made to modify the views.py

# Create your views here.
from django.http import JsonResponse
from .models import StudentModel,SubjectModel, TeacherModel
from rest_framework import viewsets
from .serializers import StudentSerializers, TeacherSerializers, SubjectSerializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CustomUser
from django.contrib.auth.models import Group

class StudentView(viewsets.ModelViewSet):
# class studentview(ListAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializers
    authentication_classes= [SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

class TeacherView(viewsets.ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers
    authentication_classes= [SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

class SubjectView(viewsets.ModelViewSet):
    queryset = SubjectModel.objects.all()
    serializer_class = SubjectSerializers
    authentication_classes= [SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    
class StudentList(APIView):

    def get(self, request, format=None):
        student= StudentModel.objects.all()
        serializer=StudentSerializers(student, many=True)
        # print(".........................",serializer.data)
    # try:
        students_group, created = Group.objects.get_or_create(name='Students')
        for data in student:
        # Create the user object
            user = CustomUser.objects.create_user(
                # username=data['email'],  # Use the email as the username
                email=data.emailf,
                password='12345',
                first_name=data.name.split()[0],
                last_name=data.name.split()[1],
                is_staff=True,
            )
        user.groups.add(students_group)
        return serializer.data
        # except:
        #     return serializer.data
# # Create the "Students" group
# students_group, created = Group.objects.get_or_create(name='Students')
# # Loop through the list of student data and create a user for each one
# for data in students:
#     # Create the user object
#     user = User.objects.create_user(
#         username=data['email'],  # Use the email as the username
#         email=data['email'],
#         password='defaultpassword',
#         first_name=data['name'].split()[0],
#         last_name=data['name'].split()[1]
#     )

#     # Add the user to the "Students" group
    #  user.groups.add(students_group)