'''
specific app urls
'''
from django.conf.urls import url
from my_app import views

#Template tagging
app_name = 'my_app'

urlpatterns = [
    url(r'^base/$', views.base, name='base'),
    url(r'^customer_list/$', views.customers, name='customers'),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^require_login/$', views.need_login, name='need_login'),
]
