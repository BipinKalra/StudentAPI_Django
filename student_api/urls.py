from django.urls import path
from student_api import views

urlpatterns = [
  path("students/", views.StudentListView.as_view()),
  path("students/<int:pk>", views.StudentDetailView.as_view()),
  path("deleteStudent/<int:pk>", views.StudentDeleteView.as_view())
  # path("createStudent/", views.createStudentAPI),
]