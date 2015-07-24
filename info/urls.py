from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^portfolio/$', views.PortfolioView.as_view(), name='portfolio'),
    url(r'^portfolio/(?P<pk>[0-9]+)/$', views.ProjectView.as_view(), name='project'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contacts/$', views.contacts, name='contacts'),
]
