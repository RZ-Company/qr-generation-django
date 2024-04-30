from django import forms

class LinkForm(forms.Form):
    link = forms.URLField(label='Enter your URL')
