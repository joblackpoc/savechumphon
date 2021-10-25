from django.core import paginator
from django.http import request, response
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
    ordering = ['campur','ctambon']
    paginate_by = 15

class SavecmpoDetailview(DetailView):
    model = Savecmpo
    template_name = 'backend/person_detail.html'

def Search(request):
    person_list = Savecmpo.objects.all()
    person_filter = PersonFilter(request.GET, queryset=person_list)
    person_filter_form = person_filter.form
    return render(request, 'backend/person_list_search.html', {'person_filter': person_filter, 'person_filter_form':person_filter_form})

class SearchList(ListView):
    model = Savecmpo
    template_name = 'backend/search_list.html'
    paginate_by = 3

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', '')
        if filter_val!='':
            persons = Savecmpo.objects.filter(Q(fname__contains=filter_val) | Q(lname__contains=filter_val) | Q(id_card__contains=filter_val) | Q(campur__contains=filter_val) | Q(ctambon__contains=filter_val))
        else:
            persons = Savecmpo.objects.all()
        return persons

    def get_context_data(self, **kwargs):
        context = super(SearchList, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', '')
        context['all_table_fields'] = Savecmpo._meta.get_fields()
        return context
