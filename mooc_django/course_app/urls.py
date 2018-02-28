# /usr/administrator/ python 27
# -*- coding: utf-8 -*-
# @Time    : 2018/1/24 15:57
# @Site    : 
# @File    : urls.py
# @Software: pycharm
from django.conf.urls import url
from course_app import views

urlpatterns = [

    # 课程列表

    url(r'^course_list/', views.course_list,name='course_list'),

    # 详情页

    url(r'^course_detail/(?P<course_id>\d+)$', views.course_detail,name='course_detail'),



]