from django import forms
from django.conf import settings

from UrlPermission.permissions.models import Role
from UrlPermission.permissions.utils import get_url_names


def get_urls():
    names = get_url_names()
    names_tuple = ()
    for name in names:
        names_tuple += ((name, name.replace('-', ' ').replace('_', ' ')),)
    return names_tuple



class RoleForm(forms.ModelForm):
    url_name = forms.MultipleChoiceField(choices=get_urls, required=False)
    users = forms.MultipleChoiceField(choices=settings.PERMISSION_APPLYED_USERS, required=False)

    class Meta:
        model = Role
        exclude = []
