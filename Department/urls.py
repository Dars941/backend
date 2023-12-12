from django.urls import path
from .views import DepartmentListCreateView, DepartmentRetrieveUpdateDestroyView

urlpatterns = [
    path('department/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('department/<int:pk>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),
]
