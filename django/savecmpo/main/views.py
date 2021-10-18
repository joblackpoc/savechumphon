from django import forms
from django.shortcuts import render,redirect
from main.forms import InputForm
from .models import Ctambon


# Create your views here.
def Home(request):

    if request.method =='POST':
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thank')
    else:
        form = InputForm()
    return render(request, 'main/home.html', {'form':form})

def thank(request):

    return render(request, 'main/thank.html')

def load_index(request):

    ampurcodefull = request.GET.get('campur')
    indexes = Ctambon.objects.filter(ampurcode_id=ampurcodefull).order_by('tambonname')
    return render(request, 'main/index_dropdown_list_option.html',{'indexes':indexes})