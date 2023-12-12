# student/urls.py
from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDestroyView

urlpatterns = [
    path('student/', StudentListCreateView.as_view(), name='student-list-create'),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),
]
