from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentsListView.as_view(), name='home'),
    path('create/', StudentCreateView.as_view(), name='new_student'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
]
