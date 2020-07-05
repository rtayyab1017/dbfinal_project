from django.contrib import admin
from .models import library_item,magazine,journal,book_collection,author,Publisher,Borrower,Borrows
# Register your models here.
admin.site.register(library_item)
admin.site.register(magazine)
admin.site.register(journal)
admin.site.register(book_collection)
admin.site.register(author)
admin.site.register(Publisher)
admin.site.register(Borrower)
admin.site.register(Borrows)
