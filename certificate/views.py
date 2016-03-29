# coding: utf-8

import mimetypes
import cStringIO as StringIO

from django.contrib import messages
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse as r, reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView
from django.core.mail import EmailMessage


from .serializer import CertificateSerializer
from .models import Certificate
from .report import PDF
# from core.utils import SendEmail


from xhtml2pdf import pisa
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


def generate_pdf(certificate):

    # template = get_template('pdf/template_pdf.html')
    # context = Context({'pagesize': 'A4', 'certificate': certificate})
    # html = template.render(context)
    # result = StringIO.StringIO()
    # pdf = pisa.pisaDocument(StringIO.StringIO(html.encode('utf-8')).read())

    pdf = PDF('pdf/template_pdf.html', [{'certificate': certificate}]).render()
    return pdf.getvalue()


def pdf_view(request, pk):

    certificate = get_object_or_404(Certificate, pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=orcamento.pdf'
    response.write(generate_pdf(certificate))

    return response


# def send_pdf(request, pk):
#     certificate = get_object_or_404(certificate, pk=pk)
#     email = EmailMessage('envio de orçamento pdf', 'teste', 'laville@laville.com', to=[certificate.email])
#     mime_type = mimetypes.guess_type('orcamento.pdf')
#     email.attach('teste', generate_pdf(certificate), mime_type[0])
#     email.send()
#     messages.info(request, 'Email enviado com sucesso!')
#     return HttpResponseRedirect("../")


class CertificateViewSet(APIView):
    serializer_class = CertificateSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(Certificate.objects.all(), many=True)
        return Response(serializer.data)
