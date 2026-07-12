from django import forms

class QRCodeForm(forms.Form):
    label = forms.CharField(
        label='Label',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'e.g. My Website, WiFi Password, Contact...'
        })
    )
    content = forms.CharField(
        label='Content (URL, text, or any data)',
        max_length=2000,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter any URL, text, phone number, Wi-Fi credentials...',
            'rows': 3,
        })
    )