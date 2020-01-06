from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.cache import never_cache

from .forms import RoleForm
from .models import Role, RoleUrl, UserRole


class RoleListView(generic.ListView):
    allow_empty = True

    template_name = '/permission/group-list.html'
    model = Role
    context_object_name = 'items'


class RoleDeleteView(generic.DeleteView):
    template_name = '/permission/group-delete.html'
    model = Role
    success_url = reverse_lazy("permission-role-list")


class RoleCreateView(generic.CreateView):
    template_name = '/permission/group-form.html'
    form_class = RoleForm
    model = Role
    success_url = reverse_lazy("permission-role-list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.roleurl_set.all().delete()
        self.object.userrole_set.all().delete()
        for url in self.request.POST.getlist('url_name'):
            RoleUrl.objects.create(role=self.object, url_name=url)
        for user_id in self.request.POST.getlist('users'):
            UserRole.objects.create(role=self.object, user_id=user_id)
        return super(RoleCreateView, self).form_valid(form)

    @never_cache
    def get(self, request, *args, **kwargs):
        self.initial['url_name'] = []
        self.initial['users'] = []
        return super(RoleCreateView, self).get(request, args, kwargs)


class RoleUpdateView(RoleCreateView, generic.UpdateView):
    @never_cache
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.initial['url_name'] = self.object.roleurl_set.values_list('url_name', flat=True)
        self.initial['users'] = self.object.userrole_set.values_list('user', flat=True)
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))
