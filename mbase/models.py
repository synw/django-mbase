# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mbase.conf import STATUSES, USER_MODEL


class MetaBaseModel(models.Model):
    edited = models.DateTimeField(editable=False, auto_now=True, verbose_name=_(u'Edited'))
    created = models.DateTimeField(editable=False, auto_now_add=True)
    editor = models.ForeignKey(USER_MODEL, null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name=_(u'Edited by'))   

    class Meta:
        abstract = True
        

class MetaBaseUniqueSlugModel(models.Model):
    slug = models.SlugField(max_length=25, unique=True)
    
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


class MetaBaseOrderedModel(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name=_(u'Order'))
    
    class Meta:
        abstract = True
        ordering = ['order']

class MetaBaseDateModel(models.Model):
    date = models.DateTimeField(editable=False, null=True, blank=True, auto_now_add=True, verbose_name=_(u'Date'))
  
    class Meta:
        abstract = True


