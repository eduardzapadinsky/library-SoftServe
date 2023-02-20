from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets

from .models import Book
from authentication.models import CustomUser
from order.models import Order
from .forms import BookForm
from .serializers import BookSerializer


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# def list_books(request):
#     # filter
#     if request.POST:
#         data = request.POST.get('data')
#         books = Book.objects.filter(description=data) | \
#             Book.objects.filter(name=data)
#         if not books:
#             try:
#                 books = Book.objects.filter(count=data)
#             except ValueError:
#                 pass
#         return render(request, 'book/list.html', {'books': books,
#                                                   'filtered': 'true'})
#     books = Book.get_all()
#     return render(request, 'book/list.html', {'books': books})

def list_books(request):
    books = Book.objects.all()
    data = []

    for book in books:
        authors = ', '.join([f'{author.name} {author.surname}' for author in book.authors.all()])
        data.append({
            'id': book.id,
            'name': book.name,
            'description': book.description,
            'authors': authors,
            'count': book.count
        })

    context = {
        'data': data
    }
    return render(request, 'book/list.html', context=context)

def books_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
        return render(request, 'book/create_book.html', {'form': form})
    else:
        data = request.POST
        Book.create(name=data['name'], description=data['description'], count=data['count'])
        return redirect(request.path)

# provide an opportunity to view a specific book (librarian/user);
def detail(request, book_id):
    book = Book.get_by_id(book_id=book_id)
    return render(request, 'book/detail.html', {'book': book})


# show all books provided to a specific user (by id) (librarian);

# @login_required(login_url='/authentication/login/')
def show_book_for_specific_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    books = []
    for i in Order.objects.all():
        if i.user.id == user_id:
            books.append(i.book)

    return render(request, 'book/user_detail_books.html', {'books': books,
                                                           'user': user})
