from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^detail/(.+)/$', views.detail, name='product_detail'),
    url(r'^product', views.product, name='product'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^signout$', views.signout, name='signout'),
    url(r'^$', views.index, name='index'),
]