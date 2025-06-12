from app_coder.models import Avatar

def avatar_usuario(request):
    avatar_url = None
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user=request.user)
            if avatar.imagen:
                avatar_url = avatar.imagen.url
        except Avatar.DoesNotExist:
            pass
    return {'avatar_url': avatar_url}