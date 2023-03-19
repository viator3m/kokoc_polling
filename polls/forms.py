from django import forms
from django.forms import RadioSelect


class AnswerForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        choice_list = [_ for _ in question.get_answers_list()]
        self.fields['answers'] = forms.ChoiceField(
            choices=choice_list, widget=RadioSelect
        )
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input mr-1'

