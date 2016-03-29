from django.conf.urls import include, url
from . import DefaultRouter


# from people.views.auth_token_view import ObtainAuthToken
# from people.views.responsible_view import ResponsibleUpdateView, ResponsibleViewSet


from certificate.views import CertificateViewSet

router = DefaultRouter()

helper_patterns = [

    # url(r'^people/$', ResponsibleViewSet.as_view(), name='people'),
    # url(r'^people/(?P<pk>[0-9]+)/$', ResponsibleUpdateView.as_view()),

    # url(r'^api-token-auth/$', ObtainAuthToken.as_view()),

    url(r'^certificate/$', CertificateViewSet.as_view(), name='certificate'),

]

urlpatterns = helper_patterns
urlpatterns.extend(router.urls)
