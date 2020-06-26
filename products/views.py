from django.shortcuts import render

# Create your views here.


def procuct_list(request):
    return render(request, 'procuct_list.html')
