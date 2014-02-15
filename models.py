# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Categorylist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=1024, blank=True)
    description = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'categoryList'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'django_site'

class Donatedlist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    donateduserid = models.ForeignKey('Usertable', db_column='donatedUserID', blank=True, null=True) # Field name made lowercase.
    categoryid = models.ForeignKey(Categorylist, db_column='categoryID', blank=True, null=True) # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=1024, blank=True) # Field name made lowercase.
    description = models.TextField(blank=True)
    imageurl = models.CharField(db_column='imageURL', max_length=1024, blank=True) # Field name made lowercase.
    equivalentpoints = models.IntegerField(db_column='equivalentPoints', blank=True, null=True) # Field name made lowercase.
    status = models.CharField(max_length=3, blank=True)
    donatedate = models.DateTimeField(db_column='donateDate') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'donatedList'

class Inprogresslist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Usertable', db_column='userID') # Field name made lowercase.
    itemid = models.ForeignKey(Donatedlist, db_column='itemID') # Field name made lowercase.
    itemstatus = models.CharField(db_column='itemStatus', max_length=3) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'inProgressList'

class Transactionlist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey(Donatedlist, db_column='itemID') # Field name made lowercase.
    posteduserid = models.ForeignKey('Usertable', db_column='postedUserID') # Field name made lowercase.
    purchaseduserid = models.ForeignKey('Usertable', db_column='purchasedUserID') # Field name made lowercase.
    ptsspent = models.IntegerField(db_column='ptsSpent') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'transactionList'

class Usertable(models.Model):
    id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pw = models.CharField(max_length=256)
    hp = models.IntegerField(blank=True, null=True)
    userright = models.IntegerField(db_column='userRight', blank=True, null=True) # Field name made lowercase.
    numdonateditem = models.IntegerField(db_column='numDonatedItem') # Field name made lowercase.
    numredeemeditem = models.IntegerField(db_column='numRedeemedItem', blank=True, null=True) # Field name made lowercase.
    imageurl = models.CharField(db_column='imageURL', max_length=1024, blank=True) # Field name made lowercase.
    userrating = models.FloatField(db_column='userRating', blank=True, null=True) # Field name made lowercase.
    jointdate = models.DateField(db_column='jointDate', blank=True, null=True) # Field name made lowercase.
    currentpoints = models.IntegerField(db_column='currentPoints', blank=True, null=True) # Field name made lowercase.
    address = models.CharField(max_length=1024, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    birthday = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True)
    class Meta:
        managed = False
        db_table = 'userTable'

