
from django.urls import path
from .views import StaffListCreateView, StaffDetailView
# Staff/urls.py
# Staff/urls.py
urlpatterns = [
    path('staff/', StaffListCreateView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
]


