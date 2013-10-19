from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def index(request):
    return redirect('rankings:index')
