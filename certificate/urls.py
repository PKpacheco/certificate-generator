from django.conf.urls import patterns, url

from .views import pdf_view

# from .views import ProposalListView, ProposalCreateView, ProposalUpdateView
#from wkhtmltopdf.views import PDFTemplateView

urlpatterns = patterns('',
                       url(r'^$', pdf_view, name='pdf_view'),
                       # url(r'^email/$', send_pdf, name='send_pdf'),
                       )
