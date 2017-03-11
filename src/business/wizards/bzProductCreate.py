from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import *
from crispy_forms.layout import *
from crispy_forms.bootstrap import *
from django.contrib.auth import get_user_model
from business.models import *
from business.forms import *
from crispy_unforms.layout import *
from formtools.wizard.views import SessionWizardView


class bzProductFormWizard_step1(businessCommonForm):
    """
    bzProductFormWizard. Step 1.
    Collects the name, code (SKU base), design and Vendor Product from the user.
    """
    form_layout = Layout(
        HTML("Step 1")
    )

    class Meta:
        model = bzProduct
        fields = ['code', 'name', 'bzDesign', 'pfProduct', ]


class bzProductFormWizard_step2(businessCommonForm):
    """
    bzProductFormWizard. Step 1.
    Assign colors and sizes
    """
    form_layout = Layout(
        HTML("Step 2")
    )

    class Meta:
        model = bzProduct
        fields = []


class bzProductFormWizard_step3(businessCommonForm):
    """
    bzProductFormWizard. Step 3.
    Confirms bzRenderings & Publish
    """
    form_layout = Layout(
        HTML("Step 3")
    )

    class Meta:
        model = bzProduct
        fields = []


class bzProductFormWizard(SessionWizardView):
    form_list = [
        bzProductFormWizard_step1,
        bzProductFormWizard_step2,
        bzProductFormWizard_step3
    ]
    template_name = "business/object_form.html"

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
