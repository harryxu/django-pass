from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import ugettext as _

from django_pass import forms

@login_required
def index(request):
    return render_to_response('index.html', RequestContext(request))

@login_required
@csrf_protect
def password_change(request):
    if request.method == 'POST':
        form = forms.PasswordChangeFrom(request.POST, request.user)
        if form.is_valid():
            form.save()
            return redirect('pass_index')
    else:
        form = forms.PasswordChangeFrom()

    return render_to_response('password_change.html', 
            RequestContext(request, {'form':form}))

