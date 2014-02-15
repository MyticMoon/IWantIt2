# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.db import connection, transaction
#import models
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, render_to_response
from random import randint
#
# def index(request):
#     t = get_template('iwantit/index.html')
#     mainBody = t.render(Context({}))
#     return render(request)
from django.views.decorators.csrf import csrf_exempt


@transaction.commit_on_success
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

@csrf_exempt
def searchitem(request):
    searchTerm = request.POST['searchTerm']
    prod_query = 'select * from donatedList where itemName like "%%' + str(searchTerm) + '%%"'
    cursor1 = connection.cursor()
    cursor1.execute(str(prod_query))
    prod_result = cursor1.fetchall()
    # template = loader.get_template('iwantit/index.html')
    # context = RequestContext(request, prod_result)
    # return HttpResponse(template.render(context))
    return render_to_response('iwantit/index.html', {'prod_result': prod_result})

def shareItAction(request):
    return render_to_response('iwantit/shareit.html', {})

@csrf_exempt
@transaction.commit_on_success
def addItemAction(request):
    if request.method != "POST":
        return HttpResponse("Bad request")
    userID = 0
    categoryID = 1
    #TODO hard code to 0 here
    itemName = request.POST.get("name")
    description = request.POST["description"]
    imageURL = request.POST.get("image")
    price = request.POST.get("price")
    point = randint(1000,5000)

    prod_query = "INSERT INTO donatedList(donatedUserID, categoryID," \
                 " itemName, description, imageURL, equivalentPoints) VALUE (%d, %d, '%s', '%s', '%s', %d)" % \
                 (userID, categoryID, itemName, description, imageURL, point)
    cursor1 = connection.cursor()
    cursor1.execute(prod_query)
    prod_result = cursor1.fetchall()
    transaction.commit()

    return render_to_response('iwantit/successadditem.html', {'point': str(point)})