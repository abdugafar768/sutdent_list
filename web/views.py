from django.views import generic
from django.urls import reverse_lazy
from .models import Students


class StudentsListView(generic.ListView):
    model = Students
    template_name = 'index.html'

class StudentCreateView(generic.CreateView):
    model = Students
    template_name = 'create_students.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class StudentUpdateView(generic.UpdateView):
    model = Students
    template_name = 'update_students.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class StudentDeleteView(generic.DeleteView):
    model = Students
    template_name = 'delete_students.html'
    success_url = reverse_lazy('home')


