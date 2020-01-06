from django.contrib.auth import get_user_model


def get_url_names():
    from django.urls import get_resolver
    urls = get_resolver().reverse_dict.keys()
    names = []
    for url in urls:
        if hasattr(url, 'url_patterns'):
            for sub_url in url.url_patterns:
                names.append(sub_url.name)
        if hasattr(url, 'name'):
            names.append(str(url.name))
        if type(url) == str:
            names.append(url)
    return names



def get_users():
    return ((user.id, user) for user in get_user_model().objects.all())
