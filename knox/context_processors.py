

def custom_user(request):
    # Only proceed if the user is authenticated
    if request.user.is_authenticated:
        return {'full_name': request.user.get_full_name()}
    else:
        return {}
