from django.db import models
from django.urls import reverse

# Create your models here.


# 文章
class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()

    def get_absolute_url(self):
        return reverse('drilldown:article_archive', kwargs={'pk': self.pk})
