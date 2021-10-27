from django.shortcuts import render

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
    return render(request, 'blog/contact.html', {'team': team_members})


def about(request):
    return render(request, 'blog/about.html', {'team': team_members})
