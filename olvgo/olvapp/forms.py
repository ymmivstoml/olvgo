from django import forms
from .models import Customer
from . import views
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class CustomerForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super(CustomerForm, self).__init__(*args, **kwargs)
       self.fields['order_id'].widget.attrs['readonly'] = True


    class Meta:
        model = Customer
        fields = (
        'order_id','full_name','company','email',
        'phone_number','note')

        widgets = {
            'order_id': forms.TextInput(attrs={'class':'orderidcls'}),
            'full_name': forms.TextInput(attrs={'class':'fullnamecls'}),
            'company': forms.TextInput(attrs={'class':'companycls'}),
            'email': forms.TextInput(attrs={'class':'emailcls'}),
            'phone_number': forms.TextInput(attrs={'class':'pncls'}),
            'note': forms.Textarea(attrs={'class':'notecls'}),

        }
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
