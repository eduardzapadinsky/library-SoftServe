from django.shortcuts import render, redirect
from rest_framework import viewsets

from .models import Author
from .forms import AuthorForm
from .serializers import AuthorSerializer


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


def create_author(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AuthorForm()
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(instance=author)
        return render(request, 'author/create_author.html', {'form': form})
    else:
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        return redirect('/author/show_authors')


# show information about all authors (librarian)
def show_authors(request):
    authors = Author.get_all()
    return render(request, 'author/show_authors.html', {'authors': authors})


# provide the ability to remove the author if he is not attached to
# any book (librarian)
def remove_author(request):
    authors = Author.get_all()
    if request.method == 'POST':
        author_id = request.POST['authors']
        if author_id != 'False':
            author = Author.objects.get(id=author_id)
            if not len(author.books.all()):
                Author.delete_by_id(author_id)
                authors = Author.get_all()
            return render(request, 'author/show_authors.html',
                          {'authors': authors,
                           'deleted_author': author})

    return render(request, 'author/remove_author.html', {'authors': authors})


def author_detail(request, id):
    author = Author.objects.get(id=id)
    return render(request,
                  'author/detail_author.html',
                  {'author': author})


def author_update(request, id):
    author = Author.objects.get(id=id)

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('band-detail', author.id)
    else:
        form = AuthorForm(instance=author)

    return render(request,
                  'author/author_update.html',
                  {'form': form})
