import django_filters
from main.models import Savecmpo

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Savecmpo
        fields = [
            'fname',
            'lname',
            'id_card',
            'campur',
            'ctambon',
        ]
