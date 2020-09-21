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
from .models import Marco

class MarcoForm(forms.ModelForm):

    class Meta:
        model = Marco
        fields = ['nombre', 'maquina', 'ancho_util', 'largo_util', 'ancho_lamina', 'largo_lamina', 'superficie']


    def __init__(self, *args, **kwargs):
        super(MarcoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.layout = Layout(
            TabHolder(
                Tab(
                    _('Informacion Basica'),
            Field('nombre', wrapper_class='col-md-12'),
            Field('maquina', wrapper_class='col-md-12'),
            Field('ancho_util',wrapper_class='col-md-6'),
            Field('largo_util',wrapper_class='col-md-6'),
            Field('ancho_lamina',wrapper_class='col-md-6'),
            Field('largo_lamina', wrapper_class='col-md-6'),
            Field('superficie', wrapper_class='col-md-12'),
                ),
            )
        )

        self.helper.layout.append(
            FormActions(
                Submit('submit', _('Submit'), css_class='btn btn-primary'),
                HTML("""{% load i18n %}<a class="btn btn-danger"
                        href="{{ url_delete }}">{% trans 'Delete' %}</a>"""),
            )
        )

