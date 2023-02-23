from email import message
import random
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import Books, RequestedBook, Student
from home.views import home
# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect(home)
    page = 'login'
    context={'page':page}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
            return render(request,'authentication/login_register.html',context)
        user = authenticate(request,username=username,password=password)
        
        if user is not None and user.is_superuser == 1:
            login(request,user)
            return render(request,'home/admin.html')
        elif user is not None and user.is_superuser == 0:
            login(request,user)
            return redirect(home)
        else:
            messages.error(request,'User name and password dosent match..')
    return render(request,'authentication/login_register.html',context)


def logoutUser(request):
    logout(request)
    return redirect(home)

def registerUser(request):
    page = 'register'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']

        if User.objects.filter(username=username).exists():
            messages.error(request,'username name is already taken..')
            context ={'username':username,'password':password,'page':page}
            return render(request,'authentication/login_register.html',context)

        User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname)
        user = authenticate(request,username=username,password=password)
        stud = Student.objects.create(name = user)
        stud.save()
        login(request,user)
        return redirect(home)
    context={'page':page}
    return render(request,'authentication/login_register.html',context)

@login_required(login_url='login')
def addStudentDetails(request):
    if request.user.is_superuser:
        return redirect(home)
    page = 'update-details'
    if Student.objects.filter(name_id = request.user.id).exists():
        stud = Student.objects.get(name_id = request.user.id)
        user = User.objects.get(id = request.user.id)
    else:
        return redirect(home)
    if request.method == 'POST':
        stud.batch = request.POST['batch']
        stud.address = request.POST['address']
        stud.branch = request.POST['branch']

        if request.POST['age']:
            stud.age = request.POST['age']

        if request.POST['admission_no']:
            stud.admission_no = request.POST['admission_no']

        if  request.POST['phone']:
            stud.phone = request.POST['phone']

        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']

        user.save()
        stud.save()

        return redirect(home)
    context={'page':page,"details":stud,'firstname':user.first_name,'lastname':user.last_name}
    return render(request,'authentication/student.html',context)

@login_required(login_url='login')
def viewStudentDetails(request,id=None):
    if request.user.is_superuser:
        return redirect(home)
    user = User.objects.get(id = request.user.id)
    stud = Student.objects.get(name_id = user.id)
    if id:
        cancel_request = RequestedBook.objects.filter(user = stud,Book_id = id)
        for i in cancel_request:
            i.delete()
    requested_books = RequestedBook.objects.filter(user = stud,issued = False)
    borrowed_books = RequestedBook.objects.filter(user = stud,issued = True)
    firstname = user.first_name
    lastname = user.last_name
    stud = Student.objects.get(name_id = request.user.id)
    context = {"stud":stud,"firstname":firstname,"lastname":lastname,"page":"view-student-details","branch":stud.get_branch_display,"requested_books":requested_books,"borrowed_books":borrowed_books}
    return render(request,'authentication/student.html',context)

@login_required(login_url='login')
def changeUsername(request):
    if request.user.is_superuser:
        return redirect(home)
    context = {"page":"change-username"}
    if request.method == 'POST':
        user = User.objects.get(username = request.user)
        uname = request.POST['username']
        passw = request.POST['password']
        if user.check_password(passw):
            if User.objects.filter(username = uname).exists():
                context['bg_color']="#ff8c00"
                context['msg'] = "username is already taken.."
                return render(request,'authentication/student.html',context)
            else:
                user.username = request.POST['username']
                msg = "User name is updated"
                context['msg'] = msg
                context['bg_color']="green"
                user.save()
        else:
            context['msg'] = 'Wrong Password ..'
            context['bg_color']="#cb341a"
    return render(request,'authentication/student.html',context)

@login_required(login_url='login')
def changePassword(request):
    if request.user.is_superuser:
        return redirect(home)
    context = {"page":"change-password"}
    msg=''
    if request.method == 'POST':
        user = User.objects.get(username = request.user)
        newPassw = request.POST['password']
        current_passw = request.POST['current_passw']

        if user.check_password(current_passw):
            if newPassw: 
                user.set_password(newPassw)
                msg = "password is updated"
            user.save()
            context['bg_color']="#00ff73"
            context['msg'] = msg
            return redirect(changePassword)
        else:
            context['msg'] = 'Wrong Password ..'
            context['bg_color']="#cb341a"
            context['border_color']="red"
            context['inp_bg']="#ffc4c4"
            context['current_passw'] = current_passw
            context['new_passw'] = newPassw
    return render(request,'authentication/student.html',context)


@login_required(login_url='login')
def requestBook(request,book_pk):
    if request.user.is_superuser:
        return redirect(home)
    book =Books.objects.get(id = book_pk)
    user = Student.objects.get(name_id = request.user.id)
    requested_book = RequestedBook.objects.create(Book = book,user = user,issued = False)
    requested_book.save()
    return redirect(home)

@login_required(login_url='login')
def returnBook(request,id):
    if request.user.is_superuser:
        return redirect(home)
    requested_book = RequestedBook.objects.get(id = id)
    if requested_book.return_request:
        requested_book.return_request = False
    else:
        requested_book.return_request = True
    requested_book.save()
    return redirect(viewStudentDetails)
# from django.http import HttpResponseRedirect
# return HttpResponseRedirect(request.path_info)