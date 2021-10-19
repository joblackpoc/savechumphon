from django.urls import path
from .views import Home, thank, load_index

urlpatterns = [
    path('', Home , name='home'),
    path('thank/',thank, name='thank'),
    path('ajax/load-index/', load_index, name='ajax-load-index'),

]
