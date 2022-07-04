from django.http import HttpResponse


def project_view(request):
    return HttpResponse("<h1>This is project view see url's file in my_app</h1>")