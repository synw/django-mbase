# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

default_statuses =  [
                     (0, _(u'Published')),
                     (1, _(u'Pending')),
                     (2, _(u'Unpublished')),
                     ]

STATUSES = getattr(settings, 'MBASE_STATUSES', default_statuses)
SLUG_MAX_LENGTH = getattr(settings, 'MBASE_SLUG_MAX_LENGTH', 25)
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)


class MetaBaseModel(models.Model):
    edited = models.DateTimeField(editable=False, auto_now=True, verbose_name=_(u'Edited'))
    created = models.DateTimeField(editable=False, auto_now_add=True)
    editor = models.ForeignKey(USER_MODEL, null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name=_(u'Edited by'))   

    class Meta:
        abstract = True
        

class MetaBaseUniqueSlugModel(models.Model):
    slug = models.CharField(max_length=25, unique=True)
    
    class Meta:
        abstract = True
        
        
class MetaBaseTitleModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_(u'Title'))
    
    class Meta:
        abstract = True
        
        
class MetaBaseShortTitleModel(models.Model):
    title = models.CharField(max_length=120, verbose_name=_(u'Title'))
    
    class Meta:
        abstract = True
        
        
class MetaBaseNameModel(models.Model):
    name = models.CharField(max_length=120, verbose_name=_(u'Name'))
    
    class Meta:
        abstract = True
        
        
class MetaBaseContentModel(models.Model):
    content = models.TextField(null=True, blank=True, verbose_name=_(u"Content"))
    
    class Meta:
        abstract = True
        
        
class MetaBaseSeoModel(models.Model):
    seo_description = models.CharField(max_length=255, null=True, blank=True, verbose_name=_(u'SEO: description'), help_text=_(u'Short description'))
    seo_keywords = models.CharField(max_length=255, null=True, blank=True, verbose_name=(u'SEO: keywords'), help_text=_(u'List of keywords separated by comas'))

    class Meta:
        abstract = True  
        

class MetaBaseStatusModel(models.Model):
    status = models.PositiveSmallIntegerField(verbose_name=_(u'Status'), choices=STATUSES, default=STATUSES[0][0])
    
    class Meta:
        abstract = True
        
        
class MetaBasePostedByModel(models.Model):
    posted_by = models.ForeignKey(USER_MODEL, null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name=_(u'Posted by'))
    
    class Meta:
        abstract = True


class OrderedModel(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name=_(u'Order'))
    
    class Meta:
        abstract = True
        ordering = ['order']

