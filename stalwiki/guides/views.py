from django.shortcuts import render

from .models import Tag, Guide


def guide_list(request):
    tags = Tag.objects.all()
    guides = Guide.objects.all()
    context = {
        'tags': tags,
        'guides': guides
    }
    return render(request, 'guides/guide_list.html', context)
