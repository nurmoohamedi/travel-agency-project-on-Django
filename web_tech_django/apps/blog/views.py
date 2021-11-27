from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import Member, Tour
from .forms import TourForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


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
    tours = Tour.objects.all()
    return render(request, 'blog/index.html', {'tours': tours})


def contact(request):
    members = Member.objects.all()

    return render(request, 'blog/contact.html', {'team': team_members, 'members': members})


def about(request):
    return render(request, 'blog/about.html', {'team': team_members})


def services(request):
    return render(request, 'blog/services.html')


@login_required(login_url='blog:login')
def addTour(request):
    # create object of form
    form = TourForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    return render(request, 'blog/add_tour.html', {'form': form})


@login_required(login_url='blog:login')
def tour_edit(request, id):
    tour = get_object_or_404(Tour, id = id)
    form = TourForm(request.POST, instance=tour)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/tour/"+id)

    return render(request, 'blog/tour_edit.html', {'form': form})


def detail_view(request, id):
    tour = Tour.objects.get(id = id)
    return render(request, "blog/detail_view.html", {'tour':tour})


@login_required(login_url='blog:login')
def tour_delete(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Tour, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "blog/tour_delete.html", context)


def tours(request):
    tours = Tour.objects.all()
    return render(request, 'blog/tours.html', {'tours': tours})


def signUp_view (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:tours')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/sign_up.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('blog:tours')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog:index')
