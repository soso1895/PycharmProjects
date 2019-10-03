from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def book(request):
#     return HttpResponse("tu shu shou ye")
#
#
# def book_detail(request,book_id):
#     text = "ni huo qu de tu shu id shi :%s" % book_id
#     return HttpResponse(text)
#
#
# def author_detail(request):
#     author_id = request.GET['id']
#     text = 'zuo zhe de id shi : %s' % author_id
#     return HttpResponse(text)

def book(request):
    return render(request, 'book.html')


