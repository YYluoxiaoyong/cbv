from django.urls import path
from books.views import PublisherList, PublisherDetail

app_name = 'books'

urlpatterns = [
    path('publishers/', PublisherList.as_view(), name='publisher_list'),
    path('publishers/<int:pk>/', PublisherDetail.as_view(), name='publisher_detail'),
]
