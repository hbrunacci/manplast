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
from .models import Pieza

class PiezaForm(forms.ModelForm):

    class Meta:
        model = Pieza
        fields = ['nombre', 'cliente', 'marco', 'material', 'espesor', 'precalentado',
                  'moldeo', 'enfriado', 'calefaccion', 'empujador', 'troquel',
                  'altura_tupir','observaciones']
        widgets = {
            'calefaccion': ImageCropWidget,
            'empujador': ImageCropWidget,

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
            Field('cliente', wrapper_class='col-md-12'),
            Field('marco',wrapper_class='col-md-4'),
            Field('material',wrapper_class='col-md-4'),
            Field('espesor',wrapper_class='col-md-4'),
            Field('precalentado', wrapper_class='col-md-12'),
            Field('moldeo', wrapper_class='col-md-12'),
            Field('enfriado', wrapper_class='col-md-12'),
                ),
                Tab(
                    _('Calefaccion'),
                    HTML('''<div class='container-flex'>
                                                                    <div class='row'>
                                                                        '''),
                    Field('calefaccion', wrapper_class='col-md-6'),
                    HTML('''
                                                                <div class=col-sm-6>
                                                                    <div class='foto_calefaccion'>
                                                                        <img id='img_calefaccion' style='width: 100px;' src="/media/{{form.calefaccion.upload_to}}{{form.calefaccion.value }}">
                                                                        </img>
                                                                       </div>
                                                                </div>
                                                            </div>
                                                        </div>
                                                '''
                         ),
                ),
                Tab(
                    _('Empujador'),
                    HTML('''<div class='container-flex'>
                                                <div class='row'>
                                                    '''),
                    Field('empujador', wrapper_class='col-md-6'),
                    HTML('''
                                            <div class=col-md-6>
                                                <div class='foto_empujador'>
                                                    <img id='img_empujador' style='width: 100px;' src="/media/{{form.empujador.upload_to}}{{form.empujador.value }}">
                                                    </img>
                                                   </div>
                                            </div>
                                        </div>
                                    </div>
                            '''
                     ),
                ),
                Tab(
                    _('Corte'),
            Field('troquel',wrapper_class='col-md-6'),
            Field('altura_tupir',wrapper_class='col-md-6'),
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

