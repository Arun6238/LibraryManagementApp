from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addbook',views.addBooks,name='addbook'),
    path('view-books',views.viewBooks,name='view-books'),
    path('test',views.testPage,name='test'),
    path('view-students',views.viewStudents,name='view-students'),
    path('view-students/<int:id>',views.viewStudents,name='view-students'),
    path('view-requested-book',views.viewRequestedBook,name='view-requested-book'),
    path('issue-book/<int:id>',views.issueBook,name='issue-book'),
    path('accept-return/<int:id>',views.acceptReturn,name='accept-return'),
    path('issued-books',views.issuedBooks,name='issued-book'),
    path('delete-book/<int:id>', views.delBook, name='delete-book'),
    path('edit-book/<int:id>',views.editBook, name='edit-book'),
]


