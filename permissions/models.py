from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Role(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('Role Name'))

    def number_of_urls(self):
        return self.roleurl_set.all().count()

    def number_of_users(self):
        return self.userrole_set.all().count()

    def __unicode__(self):
        return self.name


class RoleUrl(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    url_name = models.CharField(max_length=500, verbose_name=_('View Name'))


class UserRole(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_('user'), on_delete=models.DO_NOTHING)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
