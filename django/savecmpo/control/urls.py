from django.urls import path
from control.views import control

urlpatterns = [
    path('', control, 'control'),
]
