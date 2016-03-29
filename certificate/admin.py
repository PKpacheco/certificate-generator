from django.contrib import admin

from django.conf.urls import include, url, patterns
from .models import Certificate
from .forms import CertificateForm

from .views import pdf_view

from django.utils.safestring import mark_safe


class CertificateAdmin(admin.ModelAdmin):
    model = Certificate
    fields = ['name', 'text_1', 'text_2', 'date', 'text_3', 'time', 'logo']
    readonly_fields = ['download']

    list_display = ['__unicode__', 'nome', ]

    def download(self, obj):
        return mark_safe("<a class='btn btn-success' href='download/'>Download</a>")

    def get_urls(self):
        urls = super(CertificateAdmin, self).get_urls()
        my_urls = patterns('',

                           url(r'^(?P<pk>[0-9]+)/download/$',
                               self.admin_site.admin_view(pdf_view), name='gerar_pdf'),
                           )

        return my_urls + urls

admin.site.register(Certificate, CertificateAdmin,)
