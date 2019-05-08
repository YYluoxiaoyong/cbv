from django.urls import path
from .views import ContactView, ThanksTemplateView
from .views import AuthorList, AuthorDetail
from .views import AuthorCreate, AuthorDelete, AuthorUpdate

app_name = 'biaodan'

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('thanks/', ThanksTemplateView.as_view(), name='thanks'),
    path('author/list/', AuthorList.as_view(), name='author-list'),
    path('author/detail/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('author/add/', AuthorCreate.as_view(), name='author-add'),
    path('author/<int:pk>/', AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', AuthorDelete.as_view(), name='author-delete'),
]