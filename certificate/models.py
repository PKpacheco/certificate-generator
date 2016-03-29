# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from certificate.report import PDF
from ckeditor.fields import RichTextField
from core.descriptions import EVENTO_DEFAULT, TEXTO1, TEXTO2, TEXTO3, DATA_DEFAULT, TEMPO_DEFAULT


class Certificate (models.Model):
    name = models.CharField(max_length=255, default=EVENTO_DEFAULT, verbose_name="Nome do evento")
    text_1 = RichTextField(max_length=255, default=TEXTO1, verbose_name="Texto 1")
    text_2 = RichTextField(max_length=255, default=TEXTO2, verbose_name="Texto 2")
    date = models.CharField(max_length=255, default=DATA_DEFAULT, verbose_name="Data do evento")
    text_3 = RichTextField(max_length=255, default=TEXTO3, verbose_name="Texto 3")
    time = models.CharField(max_length=255, default=TEMPO_DEFAULT, verbose_name="Tempo do evento")
    logo = models.ImageField(upload_to='logo/', verbose_name="Logo do evento")

    def __unicode__(self):
        return unicode(self.date)

    def nome(self):
        return self.name


class Meta:
    verbose_name = 'Certificado'
    verbose_name_plural = 'Certificados'
    ordering = ['name', 'date']
