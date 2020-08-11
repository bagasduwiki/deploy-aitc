import django_filters
from django_filters import *

from .models import *

class filterpenanganan(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    # end_date = DateFilter(field_name="date_created", lookup_expr="lte
    class Meta:
        model = Pengaduans
        fields = ['kategori_penanganan']
