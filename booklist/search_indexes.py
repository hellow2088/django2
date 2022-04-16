import datetime
from haystack import indexes
from .models import Book

class BookSearch(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True,use_template=True)

	def get_model(self):
		return Book


	def index_queryset(self, using=None):  # 重载index_..函数
		"""Used when the entire index for model is updated."""
		# return self.get_model().objects.filter(updated__lte=datetime.datetime.now())
		b = Book.objects.all()
		# print(b)
		return self.get_model().objects.filter(status='p')

	 # def index_queryset(self, using=None):
        # return self.get_model().objects.filter(status='p')