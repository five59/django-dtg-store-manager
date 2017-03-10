from django_filters import *
from business.models import *
from django import forms

from crispy_forms.helper import *
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

from .models import *


class pfCatalogProductFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(pfCatalogProductFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

        col_1 = Layout("brand")
        col_2 = Layout("ptype")
        col_3 = Layout(
            Div(
                HTML("""
                <div class="btn-group">
                    <button type="submit" class="btn btn-primary btn-sm">Filter</button>
                    <a href="{{ request.path }}" class="btn btn-default btn-sm">Reset</a>
                </div>
                """),
                css_class="btn-group pull-right",
                role="group"
            )
        )

        self.helper.layout = Layout(
            Div(col_1, col_2, col_3)
        )


class pfCatalogProductFilter(FilterSet):

    brand = ModelChoiceFilter(
        label="Brand",
        queryset=pfCatalogBrand.objects.all(),
    )
    ptype = ModelChoiceFilter(
        label="Type", queryset=pfCatalogType.objects.all())

    class Meta:
        model = pfCatalogProduct
        fields = ['brand', 'ptype']
        form = pfCatalogProductFilterForm
