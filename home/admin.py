from django.contrib import admin
from .models import * 
# Register your models here.
admin.site.register(Books)
admin.site.register(Student)
admin.site.register(History)
admin.site.register(BookCount)
admin.site.register(RequestedBook)