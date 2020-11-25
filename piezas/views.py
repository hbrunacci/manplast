from django.shortcuts import render
from cruds_adminlte.crud import CRUDView
from cruds_adminlte.inline_crud import InlineAjaxCRUD
from .models import Pieza, Cortes, Rebabado,Embalado,Pegamento
from .forms import PiezaForm, CortesForm, EmbaladoForm,PegamentoForm,RebabadoForm
from django.utils.translation import ugettext_lazy as _


class RebabadoAjaxCRUD(InlineAjaxCRUD):
    model = Rebabado
    base_model = Pieza
    add_form = RebabadoForm
    update_form = RebabadoForm
    inline_field = 'pieza'
    list_fields = ['herramienta', 'detalle']
    views_available = ['create', 'update', 'list']
    paginate_by = 52
    title = _("Rebabado")

class EmbaladoAjaxCRUD(InlineAjaxCRUD):
    model = Embalado
    base_model = Pieza
    add_form = EmbaladoForm
    update_form = EmbaladoForm
    inline_field = 'pieza'
    list_fields = ['tipo_embalaje', 'detalle']
    views_available = ['create', 'update', 'list']
    paginate_by = 52
    title = _("Embalado")

class PegamentoAjaxCRUD(InlineAjaxCRUD):
    model = Pegamento
    base_model = Pieza
    add_form = PegamentoForm
    update_form = PegamentoForm
    inline_field = 'pieza'
    list_fields = ['tipo_pegamento', 'detalle']
    views_available = ['create', 'update', 'list']
    paginate_by = 52
    title = _("Pegamento")

class CortesAjaxCRUD(InlineAjaxCRUD):
    model = Cortes
    base_model = Pieza
    add_form = CortesForm
    update_form = CortesForm
    inline_field = 'pieza'
    list_fields = ['tipo_corte', 'detalle']
    views_available = ['create', 'update', 'list']
    paginate_by = 52
    title = _("Cortes")

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
    inlines = [CortesAjaxCRUD,RebabadoAjaxCRUD,PegamentoAjaxCRUD,EmbaladoAjaxCRUD]


# Create your views here.
