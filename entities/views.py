from django.shortcuts import render

from .models import Student, Instructor, Grade
from .serializer import StudentSerializer, InstructorSerializer, GradeSerializer
from rest_framework import generics
from rest_framework.views import APIView

# Create your views here.
class StudentMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentList(StudentMixin, generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing Students.

    post:
    Create a new Student instance.
    """
    pass

class StudentDetail(StudentMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a specific student

    put:
    Return a specific student to update it.

    delete:
    Return a specific student to delete it.
    """
    pass



class InstructorMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorList(InstructorMixin, generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing Instructors.

    post:
    Create a new Instructor instance.
    """
    pass

class InstructorDetail(InstructorMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a specific Instructor

    put:
    Return a specific Instructor to update it.

    delete:
    Return a specific Instructor to delete it.
    """
    pass



class GradeMixin(object):
    """
    Mixin to inherit from.
    Here we're setting the query set and the serializer
    """
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class GradeList(GradeMixin, generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing Grades.

    post:
    Create a new Grade instance.
    """
    pass

class GradeDetail(GradeMixin, generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return a specific Grade

    put:
    Return a specific Grade to update it.

    delete:
    Return a specific Grade to delete it.
    """
    pass
