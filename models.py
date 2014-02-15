# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Categorylist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=1024L, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        db_table = 'categoryList'

class Donatedlist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    donateduserid = models.ForeignKey('Usertable', null=True, db_column='donatedUserID', blank=True) # Field name made lowercase.
    categoryid = models.ForeignKey(Categorylist, null=True, db_column='categoryID', blank=True) # Field name made lowercase.
    itemname = models.CharField(max_length=1024L, db_column='itemName', blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    imageurl = models.CharField(max_length=1024L, db_column='imageURL', blank=True) # Field name made lowercase.
    equivalentpoints = models.IntegerField(null=True, db_column='equivalentPoints', blank=True) # Field name made lowercase.
    status = models.CharField(max_length=3L, blank=True)
    donatedate = models.DateTimeField(db_column='donateDate') # Field name made lowercase.
    class Meta:
        db_table = 'donatedList'

class Inprogresslist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Usertable', db_column='userID') # Field name made lowercase.
    itemid = models.ForeignKey(Donatedlist, db_column='itemID') # Field name made lowercase.
    itemstatus = models.CharField(max_length=3L, db_column='itemStatus') # Field name made lowercase.
    class Meta:
        db_table = 'inProgressList'

class Transactionlist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey(Donatedlist, db_column='itemID') # Field name made lowercase.
    posteduserid = models.ForeignKey('Usertable', db_column='postedUserID') # Field name made lowercase.
    purchaseduserid = models.ForeignKey('Usertable', db_column='purchasedUserID') # Field name made lowercase.
    ptsspent = models.IntegerField(db_column='ptsSpent') # Field name made lowercase.
    class Meta:
        db_table = 'transactionList'

class Usertable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100L)
    email = models.CharField(max_length=100L)
    pw = models.CharField(max_length=256L)
    hp = models.IntegerField(null=True, blank=True)
    userright = models.IntegerField(null=True, db_column='userRight', blank=True) # Field name made lowercase.
    numdonateditem = models.IntegerField(db_column='numDonatedItem') # Field name made lowercase.
    numredeemeditem = models.IntegerField(null=True, db_column='numRedeemedItem', blank=True) # Field name made lowercase.
    imageurl = models.CharField(max_length=1024L, db_column='imageURL', blank=True) # Field name made lowercase.
    userrating = models.FloatField(null=True, db_column='userRating', blank=True) # Field name made lowercase.
    jointdate = models.DateField(null=True, db_column='jointDate', blank=True) # Field name made lowercase.
    currentpoints = models.IntegerField(null=True, db_column='currentPoints', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'userTable'

