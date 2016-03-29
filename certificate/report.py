# coding: utf-8
import os
import StringIO
from xhtml2pdf import pisa
from xhtml2pdf.pdf import pisaPDF

from django.template.loader import render_to_string
from django.conf import settings


def link_callback(uri, rel):
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/
    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl))
    return path


class PDF(object):
    def __init__(self, template, dataset=[]):
        self.template = template
        self.dataset = dataset
        self.pdf_base = pisaPDF()

    def render(self):
        for di in self.dataset:
            page = render_to_string(self.template, di)
            self.create_page(page)
        return self.pdf_base

    def create_page(self, page):
        data = StringIO.StringIO(page.encode('utf-8'))
        temp = StringIO.StringIO()

        pdf = pisa.pisaDocument(data, temp)

        self.pdf_base.addDocument(pdf)
