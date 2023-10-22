from django import forms
from .models import Visit

INPUT_CSS_CLASS = 'form-control'


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            field.widget.attrs['class'] = INPUT_CSS_CLASS
