from UrlPermission.permissions.extras import clear_session
from UrlPermission.permissions.utils import get_url_names, get_users

PERMISSION_PATHS = [
    'dont-allow',

]
PERMISSION_EXCLUDED_PATHS = [
    'logout',
    'login',
]

PERMISSION_SUPERUSER_PASS = True
PERMISSION_STAFF_PASS = False
PERMISSION_EXTRA_URLS = [
    '/search/',
    '/search/',
]

PERMISSION_EXTRA_FUNCTION = clear_session
PERMISSION_URL_NAMES = get_url_names
PERMISSION_APPLIED_USERS = get_users
