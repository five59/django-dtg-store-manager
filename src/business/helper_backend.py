from django_tables2 import SingleTableView
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib import messages


class commonListView(SingleTableView):
    model = None
    table_class = None

    object_name = None
    object_icon = None

    template_name = "business/object_list.html"

    action_new = None
    action_list = None

    active_app = None
    active_apptitle = None

    table_pagination = {'per_page': 15}

    def get_context_data(self, **kwargs):
        context = super(commonListView, self).get_context_data(**kwargs)
        context['active_app'] = self.active_app
        context['active_apptitle'] = self.active_apptitle
        context['object_icon'] = self.object_icon
        context['object_name'] = self.object_name
        if self.action_new:
            context['action_new'] = self.action_new
        if self.action_list:
            context['action_list'] = self.action_list
        return context


class commonCreateView(CreateView):
    model = None
    form_class = None

    object_name = None
    object_icon = None

    template_name = "business/object_form.html"
    success_url = None
    action_list = None

    active_app = None
    active_apptitle = None

    def get_context_data(self, **kwargs):
        context = super(commonCreateView, self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = self.active_app
        context['active_apptitle'] = self.active_apptitle
        context['object_icon'] = self.object_icon
        context['object_name'] = self.object_name
        context['action_list'] = self.action_list
        return context


class commonUpdateView(UpdateView):
    model = None
    form_class = None

    object_name = None
    object_icon = None

    template_name = "business/object_form.html"
    success_url = None
    action_list = None

    active_app = None
    active_apptitle = None

    def get_context_data(self, **kwargs):
        context = super(commonUpdateView, self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = self.active_app
        context['active_apptitle'] = self.active_apptitle
        context['object_icon'] = self.object_icon
        context['object_name'] = self.object_name
        context['action_list'] = self.action_list
        return context


def cleanValue(value, default=""):
    return value if value else default

# class SuccessMessageMixin:
#     """
#     Add a success message on successful form submission.
#     """
#     success_message = ''
#
#     def form_valid(self, form):
#         response = super().form_valid(form)
#         success_message = self.get_success_message(form.cleaned_data)
#         if success_message:
#             messages.success(self.request, success_message)
#         return response
#
#     def get_success_message(self, cleaned_data):
# return self.success_message % cleaned_data
#
#
# class MessageMixin:
#     """
#     Add a message on next screen
#     """
#     message = ''
#
