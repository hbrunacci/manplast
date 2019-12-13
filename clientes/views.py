from django.shortcuts import render
from cruds_adminlte.crud import CRUDView
from .models import Cliente

class ClienteCRUD(CRUDView):
    model = Cliente
    namespace = None
    check_login = True
    check_perms = True
    views_available = ['create', 'list', 'delete', 'update', 'detail']


# Create your views here.
