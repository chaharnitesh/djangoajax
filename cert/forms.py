from django import forms
from .models import CertificateRecipient

class CertificateRecipientForm(forms.ModelForm):
    class Meta:
        model=CertificateRecipient
        fields = ('name','description','image')