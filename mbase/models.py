# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from autoslug import AutoSlugField


default_statuses =  [
                     (0, _(u'Published')),
                     (1, _(u'Pending')),
                     (2, _(u'Unpublished')),
                     ]

STATUSES = getattr(settings, 'MBASE_STATUSES', default_statuses)
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)


class MetaBaseModel(models.Model):
    edited = models.DateTimeField(editable=False, auto_now=True, verbose_name=_(u'Edited'))
    created = models.DateTimeField(editable=False, auto_now_add=True)
    editor = models.ForeignKey(USER_MODEL, null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name=_(u'Edited by'))   

    class Meta:
        abstract = True
        
        
class MetaBaseSlugedModel(models.Model):
    slug = AutoSlugField(unique=True, populate_from='title')
    
    class Meta:
        abstract = True
        
        
class MetaBaseTitledModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_(u'Title'))
    
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
        

class MetaBaseStatusedModel(models.Model):
    status = models.PositiveSmallIntegerField(verbose_name=_(u'Status'), choices=STATUSES, default=STATUSES[0][0])
    
    class Meta:
        abstract = True
        
        
class MetaBasePostedByModel(models.Model):
    posted_by = models.ForeignKey(USER_MODEL, null=True, blank=True, related_name='+', on_delete=models.SET_NULL, verbose_name=_(u'Posted by'))
    
    class Meta:
        abstract = True








