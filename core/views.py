from django.shortcuts import render, get_object_or_404, redirect
from manga.models import Tag, Manga, Chapter
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
#Trang chủ
def frontpage(request):
    manga = Manga.objects.all()
    tags = Tag.objects.all()
    chapters = Chapter.objects.all()
    return render(request, 'core/frontpage.html', {
        'mangas' : manga,
    })
#tìm kiếm theo tên
def searchpage(request):
    if request.method == "POST":
        searched = request.POST['searched']
        mangas = Manga.objects.filter(name__contains = searched)
        return render(request, "core/searchpage.html", {
            'searched': searched,
            'mangas': mangas
        })
    return render(request, "core/searchpage.html", {

    })

#đăng kí 
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

#Tab Truyện hot
def mangaByLikes(request):
    mangas = Manga.objects.all()
    sorted_mangas = sorted(mangas, key = lambda x: x.like_count(), reverse=True)
    return render(request, 'core/mangaByLikes.html', {
        'sorted_mangas': sorted_mangas
    })
#Danh sách truyện đã thích của user
@login_required
def likedManga(request):
    mangas = Manga.objects.all().filter(like = request.user)
    return render(request, 'core/likedManga.html', {
        'mangas': mangas
    })
#Tìm kiếm nâng cao
def filterView(request):
    tags = Tag.objects.all()
    mangas = Manga.objects.all()
    name_contains_query = request.GET.get('name_contains')
    author_query = request.GET.get('author')
    tag_list = request.GET.getlist('tags')
    sort = request.GET.get('sort')
    print(sort)
    if name_contains_query != '' and name_contains_query is not None:
        mangas = mangas.filter(name__icontains = name_contains_query)
    if author_query != '' and author_query is not None:
        mangas = mangas.filter(author__name__icontains = author_query)
    if len(tag_list) != 0:
        mangas = mangas.filter(tag__name__in = tag_list)
    if sort == 'A-Z':
        mangas = mangas.order_by('name')
    elif sort == 'Z-A':
        mangas = mangas.order_by('-name')
    elif sort == 'Ngay Cap Nhat Giam Dan':
        mangas = mangas.order_by('-updated')
    elif sort == 'Ngay Cap Nhat Tang Dan':
        mangas = mangas.order_by('-updated')
    elif sort == 'Luot thich Giam Dan':
        mangas = sorted(mangas, key = lambda x: x.like_count(), reverse=True)
    elif sort == 'Luot thich Tang Dan':
        mangas = sorted(mangas, key = lambda x: x.like_count())
    return render(request, 'core/filterView.html', {
        'tags': tags,
        'mangas': mangas
    })