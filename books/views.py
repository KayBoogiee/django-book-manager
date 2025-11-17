from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})

def book_create(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        description = request.POST["description"]
        published_year = request.POST["published_year"]

        Book.objects.create(
            title=title,
            author=author,
            description=description,
            published_year=published_year
        )
        return redirect("book_list")

    return render(request, "books/book_form.html")

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.description = request.POST["description"]
        book.published_year = request.POST["published_year"]
        book.save()

        return redirect("book_list")

    return render(request, "books/book_form.html", {"book": book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("book_list")
