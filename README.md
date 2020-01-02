# django-url-permissions

Django url permissions was created to handle user role permission by url, so if you need to create a serten role and give that role permission to that url, then you can use this package.

What does it do?
- 
it creates a middleware where it reads the url and check if the url in the path apply to the required path (such as dashboard urls or admin urls) and checks the user permission for that path.

Additional features:
- 

- you add an extra function to run on the middleware.
- you can pass a list of urls not to be check.
  