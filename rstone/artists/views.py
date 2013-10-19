from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from artists.models import Artist

def index(request, t='artists/index.html'):
    d={
        'artists':Artists.objects.all()
    }
    return render_to_response(t, d, RequestContext(request))

def detail(request,slug_artist,t='artists/detail.html'):
    artist = get_object_or_404(Artist,slug=slug_artist)
    d={
        'artist':artist,
    }
    return render_to_response(t, d, RequestContext(request))