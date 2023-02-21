from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date,timedelta

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    books=Books.objects.filter(
    Q(name__contains=q) |
    Q(auther__contains=q) |
    Q(edition__contains=q) 
    )
    if request.user.is_authenticated:
        reqBook = RequestedBook.objects.filter(user__name__id = request.user.id,)
        requested_book_id = []
        for i in reqBook:    
            requested_book_id.append(i.Book.id)
        context = {'books':books,'q':q,"reqBook":requested_book_id}
        return render(request,'home.html',context)

    context = {'books':books,'q':q}
    return render(request,'home.html',context)


@login_required(login_url='login')
def testPage(request):
    if not request.user.is_superuser:
        return redirect(home)
    books = Books.objects.all()
    context = {'books':books}
    return render(request,'home/admin.html',context)

@login_required(login_url='login')
def addBooks(request):
    if not request.user.is_superuser:
        return redirect(home)
    if request.method == 'POST':
        name =  request.POST['name']
        auther = request.POST['auther']
        language = request.POST['language']
        publisher = request.POST['publisher']
        if request.POST['publish_date']:
            publish_date = request.POST['publish_date']
        else:
            publish_date = None
        genre = request.POST['genre']
        summary = request.POST['summary']

        if len(request.FILES) != 0:
            print("book present")
            image = request.FILES['image']
            book = Books.objects.create(name=name,auther=auther,language=language,publisher=publisher,publish_date=publish_date,edition=genre,summary=summary,image= image)
        else:
            book = Books.objects.create(name=name,auther=auther,language=language,publisher=publisher,publish_date=publish_date,edition=genre,summary=summary)
        book.save()
        return render(request,'home/admin.html',{'form':True,'msg':'Book saved successfully....'})
    return render(request,'home/admin.html',{'form':True})

@login_required(login_url='login')
def viewBooks(request):
    if not request.user.is_superuser:
        return redirect(home)
    q=request.GET.get('q') if request.GET.get('q') is not None else ''
    books = Books.objects.filter(
        Q(name__contains = q) |
        Q(auther__contains = q) |
        Q(summary__contains = q)
    )
    if books :
        context = {'books':books,'q':q}
        return render(request,'home/admin.html',context)

    context = {'books':'none','q':q}
    return render(request,'home/admin.html',context)  

@login_required(login_url='login')
def editBook(request,id):
    if not request.user.is_superuser:
        return redirect(home)
    book = Books.objects.get(id = id)
    if request.method == "POST":
        book.name = request.POST['name']
        book.auther = request.POST['auther']
        book.language = request.POST['language']
        book.publisher = request.POST['publisher']
        book.publish_date = request.POST['publish_date']
        book.edition = request.POST['genre']
        book.summary = request.POST['summary']
        if len(request.FILES) != 0:
            book.image = request.FILES['image']
        book.save()
        return redirect(viewBooks)
    books = Books.objects.all()
    date = book.publish_date.strftime("%Y-%m-%d")
    print(date)
    context = {'books':books,'editBook':book,'date':date}
    return render(request,'home/admin.html',context)


@login_required(login_url='login')
def viewStudents(request,id = None):
    if not request.user.is_superuser:
        return redirect(home)
    context={'page':"view-students"}
    
    if id:
        stud = Student.objects.get(id =id)
        activity = History.objects.filter(student = stud)
        context["activity"]= activity
    
    students = Student.objects.all()
    context['students'] = students
    return render(request,'home/admin.html',context)

@login_required(login_url='login')
def viewRequestedBook(request):
    if not request.user.is_superuser:
        return redirect(home)
    page = "issue-book"
    books = RequestedBook.objects.filter(issued = False)
    context = {'reqBooks':books,"page":page}
    return render(request,'home/admin.html',context)

@login_required(login_url='login')
def issueBook(request,id):
    if not request.user.is_superuser:
        return redirect(home)
    book = RequestedBook.objects.get(id = id)
    book.issued  = True
    book.save()
    return redirect(viewRequestedBook)

@login_required(login_url='login')
def issuedBooks(request):
    if not request.user.is_superuser:
        return redirect(home)
    page = "issued-books"
    issueBook = RequestedBook.objects.filter(issued = True)
    context = {'issuedBooks':issueBook}
    context['page'] = page
    return render(request,'home/admin.html',context)

@login_required(login_url='login')
def acceptReturn(request,id):
    if not request.user.is_superuser:
        return redirect(home)
    obj = RequestedBook.objects.get(id = id)
    stud = obj.user
    book = obj.Book  
    history =History.objects.create(book= book ,student = stud,borrow_date = obj.borrow_date,return_date =date.today() )
    history.save()
    obj.delete()
    return redirect(issuedBooks)

@login_required(login_url='login')
def delBook(request,id):
    if not request.user.is_superuser:
        return redirect(home)
    book = Books.objects.get(id=id)
    book.delete()
    return redirect(viewBooks)