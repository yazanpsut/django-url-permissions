from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^role/list$', RoleListView.as_view(), name='permission-role-list'),
    url(r'^role/create$', RoleCreateView.as_view(), name='permission-role-create'),
    url(r'^role/update/(?P<pk>\d+)$', RoleUpdateView.as_view(),
        name='permission-role-update'),
    url(r'^role/delete/(?P<pk>\d+)$', RoleDeleteView.as_view(),
        name='permission-role-delete'),
    ]