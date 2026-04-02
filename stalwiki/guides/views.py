from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Tag, Guide
from .forms import GuideCreateForm


def guide_list(request):
    tags = Tag.objects.all()
    guides = Guide.objects.all()
    context = {
        'tags': tags,
        'guides': guides
    }
    return render(request, 'guides/guide_list.html', context)

@login_required
def guide_create(request):
    if request.method == 'POST':
        form = GuideCreateForm(request.POST)
        if form.is_valid():
            guide = form.save(commit=False)
            guide.user = request.user
            guide.save()
            form.save_m2m()
            return redirect('guides:guide_list')
    else:
        form = GuideCreateForm()

    context = {'form': form}
    return render(request, 'guides/guide_create.html', context)

def guide_detail(request, guide_id):
    pass
