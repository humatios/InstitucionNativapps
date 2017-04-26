from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url( r'^student/$', views.StudentList.as_view(), name = 'student_list'),
    url( r'^student/(?P<pk>[0-9]+)$', views.StudentDetail.as_view(), name = 'student_detail'),

    url( r'^instructor/$', views.InstructorList.as_view(), name = 'instructor_list'),
    url( r'^instructor/(?P<pk>[0-9]+)$', views.InstructorDetail.as_view(), name = 'instructor_detail'),

    url( r'^grade/$', views.GradeList.as_view(), name = 'grade_list'),
    url( r'^grade/(?P<pk>[0-9]+)$', views.GradeDetail.as_view(), name = 'grade_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
