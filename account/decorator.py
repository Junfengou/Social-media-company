from django.http import HttpResponse
from django.shortcuts import redirect


# I brought this over from my other website, it basically deal with user permission and what not
# Not sure what to use it on just yet but we'll figure it out as we build more features

# This calls the function in views.py to check if the user is authenticated.
# if the user is authenticated, they shouldn't be able to see the log in page or the register page
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('blog-home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# Handles permission and show what user have access to what info
def allowed_users(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("'You're not authorized to view this page")

        return wrapper_func

    return decorator
