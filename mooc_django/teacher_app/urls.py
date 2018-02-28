# /usr/administrator/ python 27
# -*- coding: utf-8 -*-
# @Time    : 2018/1/24 11:19
# @Site    : 
# @File    : urls.py
# @Software: pycharm

from django.conf.urls import url
from teacher_app import views

urlpatterns = [
    # 每位老师的url
    url(r'^teachers_detail/(?P<teacher_id>\d+)$', views.teacher_detail,name='teacher_detail'),

    # 教师列表的url
    url(r'^teachers_list/', views.teachers_list,name='teachers_list'),




]