# django-url-permissions

Django url permissions was created to handle user role permission by url, so if you need to create a certain role and give that role permission to that url, then you can use this package.

What does it do?
- 
it creates a middleware where it reads the url and check if the url in the path apply to the required path (such as dashboard urls or admin urls) and checks the user permission for that path.

Additional features:
- 

- you add an extra function to run on the middleware.
- you can pass a list of urls not to be check.

Usage
-

- add `'UrlPermission'` to your `INSTALLED_APPS`
- add `'UrlPermission.permissions.middlewares.UrlPermissionMiddleware'` to your `MIDDLEWARE`
- define the paths you need to run permissions on like:
```Python
PERMISSION_PATHS = [
    'dashboard/',
    'en/mysecret/path'
]
```
the last step will include any url containing any path in `PERMISSION_PATHS`

Extras
-
The above code is enough to run the permissions on list of paths, but there are few extra features you use with `django-url-permissions` as the following:
- Ignore any path in the settings variable `PERMISSION_EXCLUDED_PATHS`
- Ignore all checks for the superuser using `PERMISSION_SUPERUSER_PASS` (default: True)
- Ignore all checks for the staff user using `PERMISSION_STAFF_PASS` (default: False)
- Run extra functions on a list of urls using `PERMISSION_EXTRA_URLS` (list of paths to be included) and `PERMISSION_EXTRA_FUNCTION` (definition reference)
- When adding a new role, define the url names that admin should choose from by changing the settings variable `PERMISSION_URL_NAMES` to a new definition reference.
- When adding a new role, define the users that will appear to the admin by the settings variable `PERMISSION_APPLIED_USERS` to a new definition reference.
- You can use the admin to add the roles and the user urls or you can add `permissions.urls` to your project and customize the templates to your theme.
  