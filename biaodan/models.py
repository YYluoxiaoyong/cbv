from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('biaodan:author-detail', kwargs={'pk': self.pk})

