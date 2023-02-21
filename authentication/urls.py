from django.urls import path
from . import views
urlpatterns = [
    path('login',views.loginUser,name='login'),
    path('logout',views.logoutUser,name='logout'),
    path('register',views.registerUser,name='register'),
    path('add-stud-details',views.addStudentDetails,name='add-stud-details'),
    path('view-stud-details',views.viewStudentDetails,name='view-stud-details'),
    path('view-stud-details/<int:id>',views.viewStudentDetails,name='view-stud-details'),
    path('return-book/<int:id>',views.returnBook,name = "return-book"),
    path('passw-update',views.changePassword,name = 'passw-update'),
    path('uname-update',views.changeUsername,name="uname-update"),
    path('request-book/<int:book_pk>',views.requestBook,name = 'request-book'),
]
