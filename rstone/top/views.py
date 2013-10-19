from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.core.urlresolvers import reverse

from top.models import Ranking, TopAlbum, TopArtist

def index(request, t='top/index.html'):
    d={
        'rankings':Ranking.objects.all()
    }
    return render_to_response(t, d, RequestContext(request))

def detail(request,slug_ranking,t='top/detail.html'):
    ranking = get_object_or_404(Ranking, slug=slug_ranking)
    positions = ranking.positions.all()
    albums=[]
    artists=[]
    for p in positions:
        if p.__class__==TopAlbum:
            albums.append(p)
        else:
            artists.append(p)
    d={
        'ranking':ranking,
        'albums':albums,
        'artists':artists,
    }
    return render_to_response(t, d, RequestContext(request))
