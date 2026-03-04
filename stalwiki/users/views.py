from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Profile


# пока что просто будем получать первый профиль в бд
def profile(request):
    user = User.objects.first()
    profile = Profile.objects.first()
    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'users/profile.html', context)
