# from django.test import TestCase
# from datetime import date, timedelta 
# # Create your tests here.
# today = date.today()
# returnDate = today + timedelta(days=10)
# if returnDate.isoweekday() == 6:
#     returnDate = returnDate + timedelta(days=2)
#     print("return_Date :",returnDate)
# if returnDate.isoweekday() == 7:    
#     returnDate = returnDate + timedelta(days=1)
#     print("return_Date :",returnDate)
# # print(returnDate.strftime("%w"))
# print(returnDate.strftime("%Y-%m-%d"))
from .models import *

obj = History.objects.all().delete()