from django.core import paginator
from django.http import request
from django.shortcuts import render
from main.models import Savecmpo
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

# Create your views here.
def Index(request):
    people = Savecmpo.objects.all()
    context = {'people':people}
    return render(request, 'backend/index.html', context)

class SavecmpoListView(ListView):
    model = Savecmpo
    template_name = 'backend/person_list.html'
    context_object_name = 'savecmpo'
    ordering = ['campur','ctambon']
    paginate_by = 15

class SavecmpoDetailview(DetailView):
    model = Savecmpo
    template_name = 'backend/person_detail.html'


