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
        fields = '__all__'
        widgets = {
            'calefaccion': ImageCropWidget,
            'empujador': ImageCropWidget,
            'observaciones': CKEditorWidget(attrs={'lang': 'es'}),
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
            Field('calefaccion',wrapper_class='col-md-4'),
                ),
                Tab(
                    _('Empujador'),
            Field('empujador',wrapper_class='col-md-4'),
                ),
                Tab(
                    _('Terminaciones'),
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

