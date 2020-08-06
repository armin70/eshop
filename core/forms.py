from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
            'subject': forms.TextInput(attrs={'placeholder': 'موضوع'}),
            'description': forms.Textarea(attrs={'placeholder': 'متن شما'})
        }
