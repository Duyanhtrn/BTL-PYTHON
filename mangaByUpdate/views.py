from django.shortcuts import render
from manga.models import Manga
# Create your views here.
def mangaByUpdate(request):
    mangas = Manga.objects.all().order_by('-updated')
    return render(request, 'mangaByUpdate.html', {
        'mangas' : mangas
    })
