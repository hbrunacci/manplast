from django.shortcuts import render
from cruds_adminlte.crud import CRUDView
from .models import Pieza
from .forms import PiezaForm


class PiezaCRUD(CRUDView):
    model = Pieza
    check_login = True
    check_perms = False
    add_form = PiezaForm
    update_form = PiezaForm
    list_fields = ['nombre', 'cliente','material']
    list_filter = ['nombre', 'cliente','material']
    views_available = ['create', 'list', 'update', 'detail', 'delete']
    search_fields = ['nombre__icontains']
    split_space_search = True
    paginate_by = 1
    paginate_position = 'Bottom'  # Both | Bottom
    paginate_template = 'cruds/pagination/enumeration.html'


# Create your views here.
