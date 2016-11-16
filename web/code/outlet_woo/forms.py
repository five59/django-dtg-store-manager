from django.forms import ModelForm
from suit_ckeditor.widgets import CKEditorWidget


class ProductForm(ModelForm):

    class Meta:
        widgets = {
            'description': CKEditorWidget(editor_options={})
        }
