from django.forms import ModelForm
from suit_ckeditor.widgets import CKEditorWidget


class SalesChannelForm(ModelForm):

    class Meta:
        widgets = {
            'description': CKEditorWidget(editor_options={})
        }


class SeriesForm(ModelForm):

    class Meta:
        widgets = {
            'note': CKEditorWidget(editor_options={}),
            'description': CKEditorWidget(editor_options={}),
        }


class DesignForm(ModelForm):

    class Meta:
        widgets = {
            'note': CKEditorWidget(editor_options={}),
            'description': CKEditorWidget(editor_options={}),
        }


class ArtistForm(ModelForm):

    class Meta:
        widgets = {
            'notes': CKEditorWidget(editor_options={}),
            'agreement': CKEditorWidget(editor_options={}),
            'description': CKEditorWidget(editor_options={}),
        }
