from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField()

class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField()