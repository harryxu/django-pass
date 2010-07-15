from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __


class PasswordChangeFrom(forms.Form):
    oldPassword = forms.CharField(label=_('Old password'), 
            widget=forms.PasswordInput)
    password = forms.CharField(label=_('New password'), 
            widget=forms.PasswordInput)
    passwordConfirm = forms.CharField(label=_('Password confirm'), 
            widget=forms.PasswordInput)

    def __init__(self, data=None, user=None, *args, **kwargs):
        self.user = user
        super(PasswordChangeFrom, self).__init__(data, *args, **kwargs)

    def clean_oldPassword(self):
        """docstring for clean_oldPassword"""
        password = self.cleaned_data['oldPassword']
        if not self.user.check_password(password):
            raise forms.ValidationError(__('Old password error.'))

        return password

    def clean_passwordConfirm(self):
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['passwordConfirm']

        if pass1 != pass2:
            raise forms.ValidationError(__('Password not match.'))
        else:
            return pass1

    def save(self):
        """docstring for save"""
        self.user.set_password(self.cleaned_data['password'])
        self.user.save()
        return self.user
