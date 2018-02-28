# -*- coding: utf-8 -*-

from django.shortcuts import render
from teacher_app.models import *

from pure_pagination import PageNotAnInteger,Paginator,EmptyPage
# Create your views here.



# 教师列表，显示教师的详细信息
def teachers_list(request):

    teacher_list = Teacher.objects.all()

    # 教师排行榜
    sort = request.GET.get('sort','')
    if sort:
        if sort == 'hot':
            teacher_list = teacher_list.order_by('-visit_num')

    teacher_order = Teacher.objects.all().order_by('-visit_num')

    # 分页

    try:
        page = request.GET.get('page',1) # 获取当前页值，默认为1
    except PageNotAnInteger: #页值异常时
        page = 1
    except EmptyPage:
        page = 1
    paginator = Paginator(teacher_list,3,request=request) # 将内容传给分页器，每页显示内容值
    teachers = paginator.page(page)  # 最终传入前端的是teacher_list

    return render(request,'teachers-list.html',locals())


# 教师详情表，包括老师的信息和课程信息
def teacher_detail(request,teacher_id):

    # 取出教师的id,对应打开教师详情表
    teacher = Teacher.objects.get(id=teacher_id)

    # 教师排行榜

    teacher_order = Teacher.objects.all().order_by('-visit_num')

    return render(request,'teacher-detail.html',locals())




