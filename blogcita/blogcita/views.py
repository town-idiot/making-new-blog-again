from django.shortcuts import render

def index(request):
    context = {
        'Title':'HEY YOU FUCKERS',
        'Content':'AWOOOOOOOOO',
    }
    return render(request, 'index.html', context)