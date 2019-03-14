from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from .models import Member
from .forms import MForm

class HomeListView(ListView):
    model = Member
    template_name = 'memform/member-list.html'

class SuccessView(TemplateView):
    template_name = 'memform/success.html'

class HomeView(CreateView):
    model = Member
    form_class = MForm
    template_name = 'memform/member-form.html'
    success_url = reverse_lazy('result')
