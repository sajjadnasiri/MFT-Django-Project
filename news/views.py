from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import News


# def index(request):
#     return HttpResponse("Main Page")


def newsView(request):
    news = News.objects.filter(active=True)
    return render(request, "home/index.html", context={"news": news})
    
def test(request):
    # name = {"names": ["sajjad", "Ali"]}
    news = News.objects.filter(active=True)
    return render(request, "test.html", context={"news": news})