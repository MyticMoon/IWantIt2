# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import connection
#import models
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
#
# def index(request):
#     t = get_template('iwantit/index.html')
#     mainBody = t.render(Context({}))
#     return render(request)

def index(request):
    prod_query = "select * from userTable"
    cursor1 = connection.cursor()
    cursor1.execute(prod_query)
    prod_result = cursor1.fetchall()
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