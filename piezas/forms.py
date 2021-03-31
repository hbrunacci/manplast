from crispy_forms.bootstrap import TabHolder, Tab, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, HTML
from django import forms
from django.utils.translation import ugettext_lazy as _
from image_cropping import ImageCropWidget

from cruds_adminlte import (DatePickerWidget,
                            TimePickerWidget,
                            DateTimePickerWidget,
                            ColorPickerWidget,
                            CKEditorWidget)
from .models import Pieza, Cortes, Rebabado, Pegamento, Embalado

class CortesForm(forms.ModelForm):

    class Meta:
        model = Cortes
        fields = ['pieza', 'tipo_corte', 'detalle', 'altura', 'tiempo', 'imagen_ref']

        labels = {
            'detalle': _('Instrucciones'),
            'altura': _('Altura (Milimetros)'),
            'tiempo': _('Tiempo (Segundos)'),
        }
        help_texts = {
            'detalle': _('Modo de accion, herramienta o programa para usar'),
            'altura': _('Valor en Milimetros'),
            'tiempo': _('Valor en Segundos'),
        }

    def __init__(self, *args, **kwargs):
        super(CortesForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('pieza', wrapper_class='col-md-12'),
            Field('tipo_corte', wrapper_class='col-md-12'),
            Field('detalle', wrapper_class='col-md-12'),
            HTML('''<div class='container-flex'><div class='row'>'''),
            Field('imagen_ref', wrapper_class='col-md-6'),
            HTML('''<div class=col-md-6><div class='foto_pieza'>
                    <img id='img_pieza' style='width: 100px;' src="/media/{{form.imagen_ref.upload_to}}{{form.imagen_ref.value }}" alt=''>
                    </img></div></div></div></div>'''),

            Field('altura', wrapper_class='col-md-4'),
            Field('tiempo', wrapper_class='col-md-4'),
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_delete }}">{% trans 'Delete' %}</a>"""),
            )
        )

class PiezaForm(forms.ModelForm):

    class Meta:
        model = Pieza
        fields = ['nombre','imagen_pieza', 'cliente', 'marco', 'material', 'espesor', 'precalentado',
                  'moldeo', 'enfriado', 'calefaccion', 'empujador','sombra','observaciones',]
        labels = {
            'precalentado': _('Precalentado (Segundos)'),
            'moldeo': _('Moldeo (Segundos)'),
            'enfriado': _('Enfriado (Segundos)'),
        }
        help_texts = {
            'marco': _('Valor en Milimetros'),
            'material': _('Valor en Milimetros'),
            'espesor': _('Valor en Milimetros'),
            'precalentado': _('Valor en Segundos'),
            'moldeo': _('Valor en Segundos'),
            'enfriado': _('Valor en Segundos'),
        }

    def __init__(self, *args, **kwargs):
        super(PiezaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    _('Informacion Basica'),
                    Field('nombre', wrapper_class='col-md-12'),
                    HTML('''<div class='container-flex'><div class='row'>'''),
                    Field('imagen_pieza', wrapper_class='col-md-6'),
                    HTML('''<div class=col-md-6><div class='foto_pieza'>
                        <img id='img_pieza' style='width: 100px;' src="/media/{{form.imagen_pieza.upload_to}}{{form.imagen_pieza.value }}" alt=''>
                        </img></div></div></div></div>'''),
                    Field('cliente', wrapper_class='col-md-12'),
                    Field('marco', wrapper_class='col-md-4'),
                    Field('material', wrapper_class='col-md-4'),

                    Field('espesor', wrapper_class='col-md-4'),
                    HTML('''<div class='container' style='width:100%;'><div class='row' style='width:100%;'>'''),
                    Field('precalentado', wrapper_class='col-md-4'),
                    Field('moldeo', wrapper_class='col-md-4'),
                    Field('enfriado', wrapper_class='col-md-4'),
                    HTML('''</div></div>'''),

                ),
                Tab(
                    _('Calefaccion'),
                   HTML('''<div class='container-flex'><div class='row'>'''),
                    Field('calefaccion', wrapper_class='col-md-6'),
                    HTML('''<div class=col-sm-6><div class='foto_calefaccion'>
                    <img id='img_calefaccion' style='width: 100px;' src="/media/{{form.calefaccion.upload_to}}{{form.calefaccion.value }}" alt=''>
                    </img></div></div></div></div>'''),
                ),
                Tab(
                    _('Empujador - Sombra'),
                    HTML('''<div class='container-flex'><div class='row'>'''),
                    Field('empujador', wrapper_class='col-md-6'),
                    HTML('''<div class=col-md-6><div class='foto_empujador'>
                    <img id='img_empujador' style='width: 100px;' src="/media/{{form.empujador.upload_to}}{{form.empujador.value }}" alt=''>
                    </img></div></div></div></div>'''),
                    HTML('''<div class='container-flex'><div class='row'>'''),
                    Field('sombra', wrapper_class='col-md-6'),
                    HTML('''<div class=col-md-6><div class='foto_sombra'><img id='img_sombra' style='width: 100px;' src="/media/{{form.sombra.upload_to}}{{form.sombra.value }}" alt=''>
                    </img></div></div></div></div>'''),
                ),
                Tab(
                    _('Observciones Generales'),
                    Field('observaciones',wrapper_class='col-md-12'),
                )
            )
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_delete }}">{% trans 'Delete' %}</a>"""),
            )
        )

class EmbaladoForm(forms.ModelForm):

    class Meta:
        model = Embalado
        fields = ['pieza','tipo_embalaje','detalle','piezas_bulto','imagen_ref']

    def __init__(self, *args, **kwargs):
        super(EmbaladoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('pieza', wrapper_class='col-md-12'),
            Field('tipo_embalaje', wrapper_class='col-md-12'),
            Field('detalle', wrapper_class='col-md-12'),
            Field('piezas_bulto', wrapper_class='col-md-12'),
            HTML('''<div class='container-flex'><div class='row'>'''),
            Field('imagen_ref', wrapper_class='col-md-6'),
            HTML('''<div class=col-md-6><div class='foto_pieza'>
                    <img id='img_pieza' style='width: 100px;' src="/media/{{form.imagen_ref.upload_to}}{{form.imagen_ref.value }}" alt=''>
                    </img></div></div></div></div>'''),
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_delete }}">{% trans 'Delete' %}</a>"""),
            )
        )
class PegamentoForm(forms.ModelForm):

    class Meta:
        model = Pegamento
        fields = ['pieza', 'tipo_pegamento', 'detalle', 'imagen_ref']

    def __init__(self, *args, **kwargs):
        super(PegamentoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('pieza', wrapper_class='col-md-12'),
            Field('tipo_pegamento', wrapper_class='col-md-12'),
            Field('detalle', wrapper_class='col-md-12'),
            HTML('''<div class='container-flex'><div class='row'>'''),
            Field('imagen_ref', wrapper_class='col-md-6'),
            HTML('''<div class=col-md-6><div class='foto_pieza'>
                    <img id='img_pieza' style='width: 100px;' src="/media/{{form.imagen_ref.upload_to}}{{form.imagen_ref.value }}" alt=''>
                    </img></div></div></div></div>'''),
        )
        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_delete }}">{% trans 'Delete' %}</a>"""),
            )
        )

class RebabadoForm(forms.ModelForm):

    class Meta:
        model = Rebabado
        fields = ['pieza','herramienta','detalle','imagen_ref']

    def __init__(self, *args, **kwargs):
        super(RebabadoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Field('pieza', wrapper_class='col-md-12'),
            Field('herramienta', wrapper_class='col-md-12'),
            Field('detalle', wrapper_class='col-md-12'),
            HTML('''<div class='container-flex'><div class='row'>'''),
            Field('imagen_ref', wrapper_class='col-md-6'),
            HTML('''<div class=col-md-6><div class='foto_pieza'>
                    <img id='img_pieza' style='width: 100px;' src="/media/{{form.imagen_ref.upload_to}}{{form.imagen_ref.value }}" alt=''>
                    </img></div></div></div></div>'''),
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_delete }}">{% trans 'Delete' %}</a>"""),
            )
        )