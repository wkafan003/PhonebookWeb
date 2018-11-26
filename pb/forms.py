from django import forms


class ContactForm(forms.Form):
    l_name = forms.CharField(label='Your name', max_length=100,)
