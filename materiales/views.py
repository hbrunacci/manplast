from django.shortcuts import render

from django.shortcuts import render
from cruds_adminlte.crud import CRUDView
from .models import Material, Marco
from .forms import MarcoForm

class MarcoCRUD(CRUDView):
    model = Marco
    add_form = MarcoForm
    update_form = MarcoForm
    namespace = None
    check_login = True
    check_perms = True
    views_available = ['create', 'list', 'delete', 'update', 'detail']


class MaterialCRUD(CRUDView):
    model = Material
    namespace = None
    check_login = True
    check_perms = True
    views_available = ['create', 'list', 'delete', 'update', 'detail']

# Create your views here.
