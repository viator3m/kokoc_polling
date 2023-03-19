from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import RadioSelect

from users import models

User = get_user_model()


class CreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            'first_name',
            'username',
            'email',
        )


class EditColorForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['color'] = forms.ChoiceField(
            choices=models.COLOR, widget=RadioSelect
        )


class EditStyleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['styles'] = forms.ChoiceField(
            choices=models.STYLES, widget=RadioSelect
        )

