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

from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect


class bzProductFormWizard_step1(businessCommonForm):
    """
    bzProductFormWizard. Step 1.
    Collects the name, code (SKU base), design and Vendor Product from the user.
    """
    form_layout = Layout(
        Div(
            HTML("""<h4>Step 1</h4>
                <p>Lorem.</p>"""),
            css_class="col-md-4"
        ),
        Div(
            Fieldset("",
                     "code",
                     "name"),
            css_class="col-md-3"
        ),
        Div(
            Fieldset("", "bzDesign", "pfProduct"),
            css_class="col-md-4"
        ),
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
        Div(
            HTML("""<h4>Step 2: Variant Matrix</h4>
                <p>You are creating a {{ wizard.form.pfProduct }}. Now, choose the combination of colors and sizes that you'd like to offer for this product.</p>"""),
            css_class="col-md-4"
        ),
        Div(
            Field('colors', css_class='chosen',),
            css_class="col-md-4"
        ),
        Div(
            Field('sizes', css_class='chosen',),
            css_class="col-md-4"
        ),
    )

    class Meta:
        model = bzProduct
        fields = ['colors', 'sizes']


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

    def get_context_data(self, **kwargs):
        context = super(bzProductFormWizard,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "product"
        context['active_apptitle'] = "Product Catalog"
        context['object_name'] = "Product"
        context['object_icon'] = "sunglasses"
        context['action_list_label'] = "Back to List"
        context['wizardstepcount'] = range(1, self.steps.count + 1)
        context['action_list'] = reverse_lazy('business:app_product_home')
        # if self.steps.step1 == 1:
        #     self.fields['sizes'] =
        #                 self.fields['employee'].queryset = Employee.objects.filter(project_id=self.instance.project_id)
        #
        if self.steps.count > self.steps.step1:
            context['action_list_save_label'] = "Next"

        return context

    def get_form_initial(self, step):
        initial = {}
        if step == '1':  # (Step 2 - zero based)
            # pfCP = self.storage.request['0-pfProduct']
            data = self.storage.get_step_data('0')
            pfCP = data.get('0-pfProduct', "")
            if pfCP:
                obj = pfCatalogProduct.objects.get(id=pfCP)
            initial['colors'] = pfCatalogProduct.get_avail_colors(obj)
            initial['sizes'] = pfCatalogProduct.get_avail_sizes(obj)
        return self.initial_dict.get(step, initial)

    def process_step(self, form):
        if self.steps.step1 == 1:
            pass
            # if(form['pfProduct']):
            #     print("YEP")
            # print(type(form))
            # print(pfCatalogProduct.get_avail_sizes(form['pfProduct']))

        elif self.steps.step1 == 2:
            pass
        elif self.steps.step1 == 3:
            pass

        return self.get_form_step_data(form)

    def done(self, form_list, form_dict, **kwargs):
        # data = [form.cleaned_data for form in form_list],
        try:
            instance = bzProduct()
            for form in form_list:
                for field, value in form.cleaned_data.items():
                    setattr(instance, field, value)
            instance.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Created new product: {}.'.format(instance))
        except Exception as e:
            messages.add_message(
                request, messages.ERROR, 'An error occurred when trying to create a new product. {}'.format(e))

        return redirect('business:app_product_home')
