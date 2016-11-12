from django.forms import ModelForm
from suit_ckeditor.widgets import CKEditorWidget


class SalesChannelForm(ModelForm):

    class Meta:
        widgets = {
            'description': CKEditorWidget(editor_options={'startupFocus': True})
        }


class ArtistForm(ModelForm):

    class Meta:
        widgets = {
            'notes': CKEditorWidget(editor_options={'startupFocus': True}),
            'agreement': CKEditorWidget(editor_options={'startupFocus': True}),
        }
