from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from .views import ArticleYearArchiveView
from .views import ArticleMonthArchiveView
from .views import ArticleWeekArchiveView
from .views import ArticleDayArchiveView
from .views import ArticleTodayArchiveView
from django.views.generic.dates import DateDetailView

from .models import Article

app_name = 'drilldown'

urlpatterns = [
    path('archive/',
         ArchiveIndexView.as_view(model=Article, date_field="pub_date"),
         name="article_archive"),
    path('<int:year>/',
         ArticleYearArchiveView.as_view(),
         name="article_year_archive"),
    # Example: /2012/08/
    path('<int:year>/<int:month>/',
         ArticleMonthArchiveView.as_view(month_format='%m'),
         name="archive_month_numeric"),
    # Example: /2012/aug/
    path('<int:year>/<str:month>/',
         ArticleMonthArchiveView.as_view(),
         name="archive_month"),
    # Example: /2012/week/23/
    path('<int:year>/week/<int:week>/',
         ArticleWeekArchiveView.as_view(),
         name="archive_week"),
    # Example: /2012/nov/10/
    path('<int:year>/<str:month>/<int:day>/',
         ArticleDayArchiveView.as_view(),
         name="archive_day"),
    path('today/',
         ArticleTodayArchiveView.as_view(),
         name="archive_today"),
    path('<int:year>/<str:month>/<int:day>/<int:pk>/',
         DateDetailView.as_view(model=Article, date_field="pub_date"),
         name="archive_date_detail"),
]
