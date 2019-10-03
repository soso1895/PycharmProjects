from django.shortcuts import render
from django.template.loader import render_to_string
# Create your views here.
from django.http import HttpResponse


# from django.shortcuts import redirect, reverse
#
#
# def index(request):
#     username = request.GET.get('username')
#     if username:
#         return HttpResponse('前台首页')
#     else:
#         return redirect(reverse('front:login'))
#
#


# def index(request):
#     html = render_to_string("index.html")
#     return HttpResponse(html)


# def index(request):
#     # context = {
#     #     'age': 20
#     # }
#     context = {
#         'books': [
#             {
#                 'name': '三国演义',
#                 'author': '罗贯中',
#                 'price': 111
#             },
#             {
#                 'name':  '水浒',
#                 'author': '施耐庵',
#                 'price': 100
#             },
#             {
#                 'name':  '西游记',
#                 'author': '武城恩',
#                 'price': 100
#             }
#
#         ],
#         'person': {
#             'username': 'zhiliao',
#             'age': 18,
#             'height': 170
#         }
#     }
#     return render(request, 'index.html', context=context)


# def index(request):
#     return render(request, 'index1.html')
#
#
# def login(request):
#     next = request.GET.get('next')
#     text = '登陆页面，登录完成要跳转的url是： %s' % next
#     return HttpResponse(text)
#
#
# def book_detail(request, book_id):
#     text = '你的图书的ID是%s' % book_id
#     return HttpResponse(text)
#
#
# def book(request):
#     return HttpResponse('读书页面')
#
#
# def movie(request):
#     return HttpResponse('电影页面')
#
#
# def city(request):
#     return HttpResponse('同城页面')

# def index(request):
#     return render(request, 'index3.html')
#
#
# def company(request):
#     return render(request, 'company.html')
#
#
# def school(request):
#     return render(request, 'school.html')


def index(request):
    return render(request, 'index4.html')

