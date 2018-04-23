from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        my_default_errors = {
            'required': 'This field is required',
            'invalid': 'Enter a valid value between 1 and 5'
        }
        fields=('content',)
        rating = forms.IntegerField(error_messages=my_default_errors)
        
