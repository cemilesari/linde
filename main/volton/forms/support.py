from __future__ import unicode_literals, absolute_import
from django.utils.translation import ugettext_lazy as _ 
from django import forms
from main.users.models import User
from main.volton.models import Support, Iletisim
from django.core.validators import MaxLengthValidator, MinLengthValidator, EmailValidator


class SupportForm(forms.ModelForm):
    class Meta : 
        model = Support
        fields = ('full_name','email','body','tel')


class SupportTRForm(forms.ModelForm):
    class Meta : 
        model = Iletisim
        fields = ('full_name','email','body','tel')