from django.shortcuts import render

# Create your views here.


def procuct_list(request):
    return render(request, 'procuct_list.html')


def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    elif request.method == 'POST':
        app_name = request.POST['名称']
        intro = request.POST['介绍']
        url = request.POST['链接']
        icon = request.POST['图标']
        image = request.POST['大图']
        return render(request, 'publish.html')
