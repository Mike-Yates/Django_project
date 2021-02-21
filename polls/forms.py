
from django import forms
from .models import Thought  # polls ?

class ThoughtsForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = [
            'thought_text',
            # 'date_posted'  this field is automatically set
        ]


