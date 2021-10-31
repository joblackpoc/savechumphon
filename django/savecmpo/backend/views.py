import datetime
from io import StringIO
from django.db import reset_queries
import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from main.models import Savecmpo, Campur, Cchangwat, Ctambon
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView
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

def Searchlist(request):

    person_list = Savecmpo.objects.all()
    person_filter = PersonFilter(request.GET, queryset=person_list)
    person_form = person_filter.form
    
    paginator = Paginator(person_filter.qs, 15)
    page = request.GET.get('page', 1)

    try:
        persons = paginator.page(page)
    except PageNotAnInteger:
        persons = paginator.page(1)
    except EmptyPage:
        persons = paginator.page(paginator.num_pages)
    
    return render(request, 'backend/search_list.html', {'persons': persons,  'person_filter':person_filter, 'person_form': person_form})

def exportexcel(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Savecmpo'+ str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Savecmpo')

    style_head_row = xlwt.easyxf("""    
        align:
        wrap off,
        vert center,
        horiz center;
        borders:
        left THIN,
        right THIN,
        top THIN,
        bottom THIN;
        font:
        name Arial,
        colour_index white,
        bold on,
        height 0xA0;
        pattern:
        pattern solid,
        fore-colour 0x19;
        """
    )
    style_data_row = xlwt.easyxf("""
        align:
        wrap on,
        vert center,
        horiz left;
        font:
        name Arial,
        bold off,
        height 0XA0;
        borders:
        left THIN,
        right THIN,
        top THIN,
        bottom THIN;
        """
    )

    # Set data row date string format.
    style_data_row.num_format_str = 'M/D/YY'
    # Define a green color style.
    style_green = xlwt.easyxf(" pattern: fore-colour 0x11, pattern solid;")
    # Define a red color style.
    style_red = xlwt.easyxf(" pattern: fore-colour 0x0A, pattern solid;")

    ws.write(0,1, 'Firstname', style_head_row) 
    ws.write(0,2, 'Lastname', style_head_row) 
    ws.write(0,3, 'Gender', style_head_row) 
    ws.write(0,4, 'Age', style_head_row) 
    ws.write(0,5, 'ID_Card', style_head_row) 
    ws.write(0,6, 'Mobile_phone', style_head_row) 
    ws.write(0,7, 'Mobile_partner', style_head_row) 
    ws.write(0,8, 'date_arrive', style_head_row) 
    ws.write(0,9, 'date_leave', style_head_row) 
    ws.write(0,10, 'Cchangwat', style_head_row) 
    ws.write(0,11, 'Ampur', style_head_row) 
    ws.write(0,12, 'Tambon', style_head_row) 
    ws.write(0,13, 'Moo', style_head_row) 
    ws.write(0,14, 'House', style_head_row) 
    ws.write(0,15, 'Duty', style_head_row) 
    ws.write(0,16, 'Vaccine', style_head_row) 
    ws.write(0,17, 'Sickness', style_head_row) 
    ws.write(0,18, 'Lab', style_head_row) 
    ws.write(0,19, 'Input_Date', style_head_row) 

    row = 1
    for person in Savecmpo.objects.all():

        ws.write(row,1, str(person.fname), style_data_row)
        ws.write(row,2, str(person.lname), style_data_row)
        ws.write(row,3, str(person.gender), style_data_row)
        ws.write(row,4, str(person.age), style_data_row)
        ws.write(row,5, str(person.id_card), style_data_row)
        ws.write(row,6, str(person.mobile_phone), style_data_row)
        ws.write(row,7, str(person.mobile_partner), style_data_row)
        ws.write(row,8, str(person.date_arrive), style_data_row)
        ws.write(row,9, str(person.date_leave), style_data_row)
        ws.write(row,10, str(person.Cchangwat), style_data_row)
        ws.write(row,11, str(person.campur), style_data_row)
        ws.write(row,12, str(person.ctambon), style_data_row)
        ws.write(row,13, str(person.moo), style_data_row)
        ws.write(row,14, str(person.house), style_data_row)
        ws.write(row,15, str(person.duty), style_data_row)
        ws.write(row,16, str(person.vaccine_pic), style_data_row)
        ws.write(row,17, str(person.sickness), style_data_row)
        ws.write(row,18, str(person.lab), style_data_row)
        ws.write(row,19, str(person.input_date), style_data_row)

        row=row+1
    
    wb.save(response)

    return response