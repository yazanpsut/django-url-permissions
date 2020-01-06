from django.http import HttpResponseForbidden
from django.urls import resolve
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class UrlPermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_superuser and getattr(settings, 'PERMISSION_SUPERUSER_PASS', True):
            return
        elif request.user.is_staff and getattr(settings, 'PERMISSION_STAFF_PASS', False):
            return

        run_permissions = False
        for in_path in settings.PERMISSION_PATHS:
            run_permissions = run_permissions or str(request.path_info).__contains__(in_path)
            if run_permissions:
                break
        # Handle Excludes
        if run_permissions:
            for out_path in getattr(settings,'PERMISSION_EXCLUDED_PATHS', []):
                run_permissions = run_permissions and not str(request.path_info).__contains__(out_path)
                if not run_permissions:
                    break
        # check permissions
        if run_permissions:
            if not request.user.is_authenticated:
                return HttpResponseForbidden()

            url_name = resolve(request.path_info).url_name

            if not request.user.userrole_set.filter(role__roleurl__url_name=url_name).exists():
                return HttpResponseForbidden()

        run_extra = False
        for in_path in getattr(settings, 'PERMISSION_EXTRA_URLS', []):
            run_extra = run_extra or str(request.path_info).__contains__(in_path)
            if run_extra:
                break
        if run_extra:
            settings.PERMISSION_EXTRA_FUNCTION(request)
