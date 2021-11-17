from django.shortcuts import render
from .models import Member

team_members = ({
    "fname": "Muhamedi",
    "lname": "Nurmuhammed",
    "bdate": 2002,
    "email": "nurmoohamedi@gmail.com",
    "phone": "+77471970242",
    "group": "ITSE-1902",
    "position": "Director/Developer"
})


def index(request):
    return render(request, 'blog/index.html')


def contact(request):
    members = Member.objects.all()

    return render(request, 'blog/contact.html', {'team': team_members, 'members': members})


def about(request):
    return render(request, 'blog/about.html', {'team': team_members})


def tours(request):
    return render(request, 'blog/tours.html')


def services(request):
    return render(request, 'blog/services.html')
