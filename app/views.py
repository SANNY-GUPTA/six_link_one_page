from django.shortcuts import render

def dummy(request):
    return render(request,'dummy.html')


def button(request):
    return render(request,'button.html')


def container(request):
    return render(request,'container.html')


def pop(request):
    return render(request,'pop.html')

def dropdown(request):
    return render(request,'dropdown.html')
