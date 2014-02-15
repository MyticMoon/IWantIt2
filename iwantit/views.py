# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import connection
#import models
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, render_to_response
#
# def index(request):
#     t = get_template('iwantit/index.html')
#     mainBody = t.render(Context({}))
#     return render(request)

def index(request):
    prod_query = "select * from donatedList"
    cursor1 = connection.cursor()
    cursor1.execute(prod_query)
    prod_result = cursor1.fetchall()
    # template = loader.get_template('iwantit/index.html')
    # context = RequestContext(request, prod_result)
    # return HttpResponse(template.render(context))
    return render_to_response('iwantit/index.html', {'prod_result': prod_result})

def profile(request):
    user_id = 0
    user_query = "SELECT name, address, birthday, gender, email, hp, imageUrl, currentPoints, numDonatedItem, numRedeemedItem FROM userTable WHERE id = " + str(user_id)
    user_cursor = connection.cursor()
    user_cursor.execute(user_query)
    user = user_cursor.fetchall()[0]
    donation_query = "SELECT categoryID, itemName, description, imageUrl, equivalentPoints, status, donateDate FROM donatedList WHERE donatedUserId = " + str(user_id)
    donation_cursor = connection.cursor()
    donation_cursor.execute(donation_query)
    donations = donation_cursor.fetchall()
    return render_to_response('iwantit/profile.html', {'user': user, 'donations': donations})

def contact(request):
    template = loader.get_template('iwantit/contact.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))