from django import forms

class Email_details(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True)
    comment = forms.CharField(label='Description', widget=forms.Textarea(attrs={'placeholder': 'Content'}), required=True)