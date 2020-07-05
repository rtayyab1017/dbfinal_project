from django.shortcuts import render
from books.models import library_item

# Create your views here.
def home(request):
    libraryitem = library_item.objects.all()
    return render(request, 'maincoverpage/home.html',{'libraryitem': libraryitem})


