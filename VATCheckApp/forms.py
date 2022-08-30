from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(label="Eine Datei auswählen")