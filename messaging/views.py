from django.shortcuts import render
from django.http import JsonResponse


def home_view(request):
    return JsonResponse({"name": "bernard"})


def about_view(request):
    return JsonResponse(
        {"Position": "CEO", "Title": "Chief Executive Officer", "Year": "2022-2023"}
    )


def list_names(request):
    return JsonResponse(
        {"data": [{"name": "bernard", "price": 500}, {"name": "chris", "price": 400}]}
    )
