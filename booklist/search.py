from .models import Book


def getBooks(request):
	pass
    # else:
    #     keyword = request.POST.get('keyword')
    #     results = Book.objects.filter(title__contains=keyword)
    #     book_counts = Book.objects.filter(title__contains=keyword).count()