from django.shortcuts import render, get_object_or_404
from manga.models import Tag, Manga
# Create your views here.
def mangaByTag(request, pk):
    tag = get_object_or_404(Tag, pk = pk)
    mangas = Manga.objects.all().filter(tag = tag)
    return render(request, 'mangaByTag.html', {
        'tag': tag,
        'mangas': mangas
    })