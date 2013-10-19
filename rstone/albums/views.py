from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from albums.models import Album,Band

def index_albums(request, t='albums/index.html'):
    d={
        'albums':Album.objects.all()
    }
    return render_to_response(t, d, RequestContext(request))

def detail_albums(request,slug_album,t='albums/detail.html'):
    album = get_object_or_404(Album,slug=slug_album)
    d={
        'album':album,
    }
    return render_to_response(t, d, RequestContext(request))

def index_bands(request, t='bands/index.html'):
    d={
        'bands':Band.objects.all()
    }
    return render_to_response(t, d, RequestContext(request))

def detail_bands(request,slug_band,t='bands/detail.html'):
    band = get_object_or_404(Band,slug=slug_band)
    d={
        'band':band,
    }
    return render_to_response(t, d, RequestContext(request))