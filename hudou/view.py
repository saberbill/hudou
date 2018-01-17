from django.http import HttpResponse


def hello(request):
    return HttpResponse("<h3>使用Django的第一个web页面</h3><hr>")