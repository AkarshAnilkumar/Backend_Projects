from django import forms
from .models import Editor
from ckeditor.widgets import CKEditorWidget

class Editorform(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="texteditor")
    class Meta:
        model = Editor
        fields = "__all__"

