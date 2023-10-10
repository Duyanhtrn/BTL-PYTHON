from django.shortcuts import render, get_object_or_404
from manga.models import Manga, Author

# Create your views here.
def author(request, pk):
    author = get_object_or_404(Author, pk = pk)
    mangas = Manga.objects.filter(author = author)
    return render(request, 'author.html',{
        'author': author,
        'mangas': mangas
    })