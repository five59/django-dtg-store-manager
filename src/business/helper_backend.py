from django_tables2 import SingleTableView


class commonListView(SingleTableView):
    model = None
    table_class = None

    object_name = None
    object_icon = None

    template_name = "business/object_list.html"

    action_new = None
    active_app = None
    active_apptitle = None

    def get_context_data(self, **kwargs):
        context = super(commonListView, self).get_context_data(**kwargs)
        context['active_app'] = self.active_app
        context['active_apptitle'] = self.active_apptitle
        context['object_icon'] = self.object_icon
        context['object_name'] = self.object_name
        return context
