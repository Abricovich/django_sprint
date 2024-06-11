from django.shortcuts import render


def about(request: str):
    return render(request, 'pages/about.html')


def rules(request: str):
    return render(request, 'pages/rules.html')
