from django.shortcuts import render
from .models import BookData, UserData, Workspace


# Create your views here.
def index(request):
    return render(request, 'index.html')


def show_books(request):
    all_books = BookData.objects.all()

    return render(request, 'show_books.html', {'all_books': all_books})


def show_users(request):
    all_users = UserData.objects.all()

    return render(request, 'show_users.html', {'all_users': all_users})


def records(request):
    entries = Workspace.objects.all()

    return render(request, 'records.html', {'entries': entries})


def add_book(request, book_id=0):
    if request.method == 'POST':
        bk_name = request.POST['bk_name']
        author = request.POST['author']
        publication = request.POST['publication']
        price = int(request.POST['price'])
        genre = request.POST['genre']
        new_book = BookData(bk_name=bk_name, author=author, publication=publication, price=price, genre_id=genre)
        new_book.save()

        message = "New book added to records"
        return render(request, 'output.html', {'message': message})

    elif request.method == "GET":

        return render(request, 'add_book.html')

    else:
        message = "Exception has occurred"
        return render(request, 'output.html', {'message': message})


def add_user(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = int(request.POST['contact'])
        address = request.POST['address']
        membership = request.POST['membership']
        new_user = UserData(fname=fname, lname=lname, contact=contact, address=address, membership_id=membership)
        new_user.save()

        message = "New user added to records"
        return render(request, 'output.html', {'message': message})

    elif request.method == "GET":

        return render(request, 'add_user.html')

    else:
        message = "Exception has occurred"
        return render(request, 'output.html', {'message': message})


def add_record(request):
    if request.method == 'POST':
        user = request.POST['user']
        book = request.POST['book']
        dt_taken = request.POST['dt_taken']
        dt_returned = request.POST['dt_returned']
        bk_status = request.POST['bk_status']
        new_record = Workspace(user_id=user, book_id=book, dt_taken=dt_taken, dt_returned=dt_returned,
                               bk_status_id=bk_status)
        new_record.save()

        message = "New user information to records"
        return render(request, 'output.html', {'message': message})



    elif request.method == "GET":

        return render(request, 'add_record.html')

    else:
        message = "Exception has occurred"
        return render(request, 'output.html', {'message': message})
