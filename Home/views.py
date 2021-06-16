from django.shortcuts import render
from django.views.generic import ListView
from Election.models import Candidates,Election
# Create your views here.
class home_view(ListView):
    model = Election
    template_name = 'home_view.html'

    def get_context_data(self, **kwargs):
        data = super(home_view, self).get_context_data(**kwargs)
        data['Election'] = Election.objects.all()
        return data


    def get_queryset(self):
        queryset = {'Election': Election.objects.all()}
        return queryset



