from django.shortcuts import render
from django.views import generic
from .models import Project


def index(request):
    test_string = 'test'
    context = {'test_string': test_string}
    return render(request, 'info/index.html', context)


def about(request):
    return render(request, 'info/about.html')


def contacts(request):
    return render(request, 'info/contacts.html')

class PortfolioView(generic.ListView):
    template_name = 'info/portfolio.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
        return Project.objects.all()


class ProjectView(generic.DetailView):
    model = Project
