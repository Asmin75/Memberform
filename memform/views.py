from django.views.generic import CreateView

from .models import Member
from .forms import MemberForm

class IndexView(CreateView):
    model = Member
    template_name = 'memform/index_form.html'
    form_class = MemberForm