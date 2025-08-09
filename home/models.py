# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Client(models.Model):

    #__Client_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    whatsapp number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)

    #__Client_FIELDS__END

    class Meta:
        verbose_name        = _("Client")
        verbose_name_plural = _("Client")


class Container(models.Model):

    #__Container_FIELDS__
    number = models.CharField(max_length=255, null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Container_FIELDS__END

    class Meta:
        verbose_name        = _("Container")
        verbose_name_plural = _("Container")


class Shipmentupdate(models.Model):

    #__Shipmentupdate_FIELDS__
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    update type = models.CharField(max_length=255, null=True, blank=True)
    booking number = models.CharField(max_length=255, null=True, blank=True)
    bl number = models.CharField(max_length=255, null=True, blank=True)
    cargo description = models.CharField(max_length=255, null=True, blank=True)
    containers = models.ForeignKey(Container, on_delete=models.CASCADE)
    vessel name = models.CharField(max_length=255, null=True, blank=True)
    origin port = models.CharField(max_length=255, null=True, blank=True)
    destination port = models.CharField(max_length=255, null=True, blank=True)
    etd = models.DateTimeField(blank=True, null=True, default=timezone.now)
    eta = models.DateTimeField(blank=True, null=True, default=timezone.now)
    status = models.CharField(max_length=255, null=True, blank=True)
    icd cfs = models.CharField(max_length=255, null=True, blank=True)
    created on = models.DateTimeField(blank=True, null=True, default=timezone.now)
    sent = models.BooleanField()

    #__Shipmentupdate_FIELDS__END

    class Meta:
        verbose_name        = _("Shipmentupdate")
        verbose_name_plural = _("Shipmentupdate")



#__MODELS__END
