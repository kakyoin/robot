from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, render


def index(request):
    return render_to_response('index.html',)