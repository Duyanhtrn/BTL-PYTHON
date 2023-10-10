from django.shortcuts import render, get_object_or_404
from .models import Manga, Tag,Chapter
from readingPage.models import Page
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.
def detail(request, pk):
    manga = get_object_or_404(Manga, pk = pk)
    tags = manga.tag.all()
    chapters = Chapter.objects.filter(manga = manga)
    liked = False
    if manga.like.filter(id = request.user.id).exists():
        liked = True
        
    return render(request, 'manga/detail.html',{
        'manga': manga,
        'tags': tags,
        'chapters': chapters,
        'author': manga.author,
        'like_count': manga.like_count(),
        'liked': liked
    })

def LikeView(request, pk):
    manga = get_object_or_404(Manga, id = request.POST.get('manga_id'))
    liked = False
    if manga.like.filter(id = request.user.id).exists():
        manga.like.remove(request.user)
        liked = False
    else:
        manga.like.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('manga:detail', args = [str(pk)]))