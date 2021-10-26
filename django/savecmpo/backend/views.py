from django.core import paginator
from django.shortcuts import render
from main.models import Savecmpo
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

class SearchListView(ListView):
    model = Savecmpo
    template_name = 'backend/search_list.html'
    context_object_name = 'persons'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PersonFilter(self.request.GET, queryset=self.get_queryset())

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        word = PersonFilter(self.request.GET, queryset=qs)
        return word.qs
