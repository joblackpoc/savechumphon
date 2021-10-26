from django.core import paginator
from django.http import request, response
from django.shortcuts import render
from main.models import Campur, Savecmpo
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView
from django.db.models import Q, query
from backend.filters import PersonFilter

# Create your views here.
def Index(request):
    people = Savecmpo.objects.all()
    context = {'people':people}

    return render(request, 'backend/index.html', context)

class SavecmpoListView(ListView):
    model = Savecmpo
    template_name = 'backend/person_list.html'
    context_object_name = 'savecmpo'
    ordering = ['campur', 'ctambon']
    paginate_by = 15

class SavecmpoDetailview(DetailView):
    model = Savecmpo
    template_name = 'backend/person_detail.html'

def Search(request):
    person_list = Savecmpo.objects.all()
    person_filter = PersonFilter(request.GET, queryset=person_list)
    person_filter_form = person_filter.form
    return render(request, 'backend/person_list_search.html', {'person_filter': person_filter, 'person_filter_form':person_filter_form})

def Search_list(request):
    person_list = Savecmpo.objects.all()
    person_filter = PersonFilter(request.GET, queryset=person_list)
    person_filter_form = person_filter.form
    
    person_filter = person_filter.qs
    paginator = Paginator(person_filter, 15)

    page = request.GET.get('page')
    try:
        response = paginator.page(page)
    except PageNotAnInteger:
        response = paginator.page(1)
    except EmptyPage:
        response = paginator.page(paginator.num_pages)
        
    return render(request, 'backend/search_list.html', {'filter':response, 'person_filter_form':person_filter_form})