from django.shortcuts import render
from .models import Article


def archive(request):
    return render(request, 'articles/archive.html', {"posts": Article.objects.all()})
