from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def book(request):
    return HttpResponse('图书首页')


def book_detail(request, book_id, category_id):
    text = "ni huo qu de tu shu id shi : %s, tu shu fen lei shi %s" % (book_id, category_id)
    return HttpResponse(text)


def author_detail(request):
    author_id = request.GET.get('id')
    text = "zuo zhe de id shi %s" % author_id
    return HttpResponse(text)
