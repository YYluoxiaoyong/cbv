from .forms import ContactForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Author

from django.contrib.auth.mixins import LoginRequiredMixin


class ContactView(FormView):
    template_name = 'biaodan/contact.html'
    form_class = ContactForm
    success_url = '/biaodan/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class ThanksTemplateView(TemplateView):

    template_name = "biaodan/thanks.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = "恭喜您成功发送了一封E-Mail"
        return context


class AuthorList(ListView):
    model = Author


class AuthorDetail(DetailView):
    model = Author


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['name']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('biaodan:author-list')
