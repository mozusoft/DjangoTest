import random

from django.shortcuts import render
from students.models import Student


# Create your views here.
def home(request):
    context = {}
    num = random.randint(1, 3)
    obj = Student.objects.get(id=num)
    print(obj)
    context['students'] = obj
    return render(request, 'students/home.html', context)
