from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'resoluteqa/index.html')
