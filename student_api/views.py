from rest_framework.decorators import api_view
from rest_framework.response import Response
from student_api import serializers, models
from rest_framework.generics import (
  ListAPIView,
  RetrieveAPIView,
  UpdateAPIView,
  RetrieveUpdateAPIView,
  ListCreateAPIView,
  DestroyAPIView
)
# Create your views here.

# class StudentListView(ListAPIView):
#   queryset = models.Student.objects.all()
#   serializer_class = serializers.StudentSerializer

class StudentListView(ListCreateAPIView):
  queryset = models.Student.objects.all()
  serializer_class = serializers.StudentSerializer

# class StudentDetailView(RetrieveAPIView):
#   queryset = models.Student.objects.all()
#   serializer_class = serializers.StudentSerializer 

class StudentDetailView(RetrieveUpdateAPIView):
  queryset = models.Student.objects.all()
  serializer_class = serializers.StudentSerializer

class StudentDeleteView(DestroyAPIView):
  queryset = models.Student.objects.all()
  serializer_class = serializers.StudentSerializer 

# @api_view()
# def StudentAPI(request):
#   students = models.Student.objects.all()
#   response = serializers.StudentSerializer(students, many = True)

#   return Response(response.data)

# @api_view(["POST"])
# def createStudentAPI(request):
#   body = json.loads(request.body)
#   response = serializers.StudentSerializer(data = body)
#   if response.is_valid():
#     inst = response.save()
#     response = serializers.StudentSerializer(inst)
#     return Response(response.data)
  
#   return Response(response.errors)


