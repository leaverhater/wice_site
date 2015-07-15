from django.shortcuts import render


def index(request):
    test_string = 'test'
    context = {'test_string': test_string}
    return render(request, 'info/index.html', context)


def about(request):
    return render(request, 'info/about.html')


def contacts(request):
    return render(request, 'info/contacts.html')
