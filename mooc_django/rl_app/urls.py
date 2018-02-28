# /usr/administrator/ python 27
# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 15:27
# @Site    : 
# @File    : urls.py
# @Software: pycharm

from django.conf.urls import url

from rl_app import views


urlpatterns = [
    # 登录注册
    url(r'^register/', views.registerView.as_view(), name='register'),

    url(r'^login/$', views.LoginView.as_view(), name='log_in'),

    url(r'^logout/$', views.log_out, name='log_out'),

    url(r'^active/(?P<active_code>.*)/$',views.ActiveUserView.as_view(),name='user_active'), # 激活码链接


]
