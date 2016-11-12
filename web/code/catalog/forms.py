from django.forms import ModelForm
from suit_ckeditor.widgets import CKEditorWidget


class BrandForm(ModelForm):

    class Meta:
        widgets = {
            'description': CKEditorWidget(editor_options={'startupFocus': True})
        }


class ItemForm(ModelForm):

    class Meta:
        widgets = {
            'description': CKEditorWidget(editor_options={'startupFocus': True})
        }
