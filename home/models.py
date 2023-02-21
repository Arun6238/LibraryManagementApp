from email.policy import default
from enum import unique
from itertools import count
from random import choices
from django.db import models
from django.contrib.auth.models import User
from datetime import date,timedelta

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=100)
    auther = models.CharField(max_length=100)
    language = models.CharField(max_length=50,null=True)
    publisher = models.CharField(max_length=100,null=True)
    publish_date = models.DateField(null=True,blank=True)
    edition = models.CharField(max_length=50,null=True)
    summary = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        if len(self.name)>32:
            return self.name[0:32]+"..."
        else:
            return self.name

class Student(models.Model):

    batch_choice = [
    ("",""),
    ("CHE", 'Computer Hardware Engineering'),
    ("EC", 'Electronocs And Communications'),
    ("ME", 'Mechanical Engineering'),
    ("IE", 'Instrumentaion Engineering'),
    ("CE", 'Computer Engineering'),
    ]

    name = models.OneToOneField(User,on_delete=models.CASCADE)
    age = models.IntegerField(null=True,blank=True)
    address = models.CharField(null=True,max_length=100,blank=True)
    phone = models.BigIntegerField(null=True,blank=True)
    admission_no = models.IntegerField(null=True,blank=True)
    branch = models.CharField(max_length=3,choices=batch_choice,null=True,blank=True)
    batch = models.CharField( max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name.get_full_name()

class History(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    borrow_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
   


class BookCount(models.Model):
    Book = models.ForeignKey(Books, on_delete=models.CASCADE)
    count = models.IntegerField()

class RequestedBook(models.Model):
    Book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    issued = models.BooleanField()
    return_request = models.BooleanField(default=False)
    borrow_date = models.DateField(null=True,blank = True)
    return_date = models.DateField(null=True,blank = True)

    def __str__(self) :
         return self.Book.name

    def save(self, *args, **kwargs):
        if self.issued == False:
            self.borrow_date = None
            self.return_date = None
        else:
            today = date.today()
            self.borrow_date = today
            returnDate = today + timedelta(days=14)

            if returnDate.isoweekday() == 6:
                    returnDate = returnDate + timedelta(days=2)

            if returnDate.isoweekday() == 7:    
                    returnDate = returnDate + timedelta(days=1)
    
            self.return_date = returnDate
        super(RequestedBook, self).save(*args, **kwargs)     
