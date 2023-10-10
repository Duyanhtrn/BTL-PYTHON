from django.shortcuts import render, get_object_or_404
from .models import Page
from manga.models import Chapter
# Create your views here.
def readingPage(request, pk):
    chapter = get_object_or_404(Chapter, pk = pk)
    pages = Page.objects.filter(chapter = chapter)
    chaplist = list(Chapter.objects.all().values_list("name", flat = True))
    currentIndex = chaplist.index(chapter.name)
    if(currentIndex == 0):
        nextChap = Chapter.objects.all()[currentIndex+1]
        return render(request, 'readingPage/readingPage.html',{
        'pages': pages,
        'chapter': chapter,
        'nextChap': nextChap,
        'numberOfChapter': Chapter.objects.all().__len__
    })
    elif currentIndex == chapter.manga.numberOfChapters:
        prevChap = Chapter.objects.all()[currentIndex-1]
        return render(request, 'readingPage/readingPage.html',{
        'pages': pages,
        'chapter': chapter,
        'prevChap': prevChap,
        'numberOfChapter': Chapter.objects.all().__len__
    })
    else:
        nextChap = Chapter.objects.all()[currentIndex+1]
        prevChap = Chapter.objects.all()[currentIndex-1]
        return render(request, 'readingPage/readingPage.html',{
            'pages': pages,
            'chapter': chapter,
            'nextChap': nextChap,
            'prevChap': prevChap,
            'numberOfChapter': Chapter.objects.all().__len__
        })
