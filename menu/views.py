from django.shortcuts import render


def base_menu(request, category=None):
    return render(request, 'menu/home.html')
