# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AppUserprofile(models.Model):
    dob = models.DateField(blank=True, null=True)
    mobile_no = models.CharField(unique=True, max_length=20, blank=True, null=True)
    education_place = models.CharField(max_length=40, blank=True, null=True)
    education_field = models.CharField(max_length=40, blank=True, null=True)
    employment_place = models.CharField(max_length=40, blank=True, null=True)
    employment_designation = models.CharField(max_length=40, blank=True, null=True)
    occupation = models.CharField(max_length=40, blank=True, null=True)
    residence_place = models.CharField(max_length=60, blank=True, null=True)
    country = models.CharField(max_length=30)
    picture = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_userprofile'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Comment(models.Model):
    c_id = models.AutoField(primary_key=True)
    text = models.TextField()
    likes = models.IntegerField()
    pt = models.ForeignKey('Post')

    class Meta:
        managed = False
        db_table = 'comment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Follows(models.Model):
    f_id = models.AutoField(primary_key=True)
    up_id_follower = models.ForeignKey(AppUserprofile, db_column='up_id_follower')
    up_id_following = models.ForeignKey(AppUserprofile, db_column='up_id_following')

    class Meta:
        managed = False
        db_table = 'follows'


class HasInterest(models.Model):
    h_i_id = models.AutoField(primary_key=True)
    up = models.ForeignKey(AppUserprofile)
    t = models.ForeignKey('Topic')

    class Meta:
        managed = False
        db_table = 'has_interest'


class HasTags(models.Model):
    h_t_id = models.AutoField(primary_key=True)
    pt = models.ForeignKey('Post')
    t = models.ForeignKey('Topic')

    class Meta:
        managed = False
        db_table = 'has_tags'


class Post(models.Model):
    pt_id = models.AutoField(primary_key=True)
    text = models.TextField()
    likes = models.IntegerField()
    up = models.ForeignKey(AppUserprofile)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'post'


class Topic(models.Model):
    name = models.CharField(max_length=120)
    t_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'topic'
