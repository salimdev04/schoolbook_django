from .models import Campus
from django.shortcuts import get_object_or_404, render

from taggit.models import Tag

# Create your views here.


def campus_list(request, tag_slug=None):
    campus_lists = Campus.published.all()
    tag = None

    print(campus_lists)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        campus_lists = campus_lists.filter(tag__in=[tag])

    return render(request, 'home/index.html', {
        'tag': tag,
        'campus_lists': campus_lists
    })


def campus_detail(request, id, slug):
    campus = get_object_or_404(Campus, slug=slug, pk=id, status='published')

    return render(request, 'campus/campus_detail', {
        'campus': campus
    })
