from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from django.template.loader import render_to_string
from django.http import HttpResponse
# def index(request):
#     username = request.GET.get('username')
#     if username:
#         return HttpResponse('front first page')
#     else:
#         return redirect(reverse('front:login'))
#
#
# def login(request):
#     return HttpResponse('front login page')


def index(request):
    # html = render_to_string('index.html')
    # return HttpResponse(html)
    return render(request, 'index.html')

