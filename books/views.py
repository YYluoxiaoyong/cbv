from django.views.generic import ListView, DetailView
from books.models import Publisher, Book
from django.utils import timezone


class PublisherList(ListView):

    model = Publisher
    template_name = "books/publisher_list.html"
    context_object_name = 'my_favorite_publishers'
    paginate_by = 4  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PublisherDetail(DetailView):

    model = Publisher
    context_object_name = 'this_publisher_information'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context
