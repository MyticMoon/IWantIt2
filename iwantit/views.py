# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Usertable
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
#
# def index(request):
#     t = get_template('iwantit/index.html')
#     mainBody = t.render(Context({}))
#     return render(request)

def index(request):
    listUser = Usertable.objects.all()
    template = loader.get_template('iwantit/index.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))

def profile(request):
    template = loader.get_template('iwantit/profile.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template('iwantit/contact.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))