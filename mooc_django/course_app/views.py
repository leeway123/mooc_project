from django.shortcuts import render
from teacher_app.models import Course
from pure_pagination import PageNotAnInteger,Paginator,EmptyPage
# Create your views here.
def course_list(request):

    courses_list = Course.objects.all() # 展示全部数据

    hot_courses = Course.objects.order_by('student_count')[0:2]

    # 课程搜索
    # search_keywords = request.GET.get('keywords','')
    # if search_keywords:
    #     all_course = courses_list.filter(Q)

    # 根据不同的标准，显示.sort是前端定义的,通过get可以获取不同的sort值，同搜索

    sort = request.GET.get('sort','')
    if sort:
        if sort == 'students': # 根据学生量
            courses_list = courses_list.order_by('-student_count')
        elif sort == 'hot': # 根据点击量
            courses_list = courses_list.order_by('-has_fav')


    # 分页
    try:
        page = request.GET.get('page',1) # 获取页值，如果没有默认为1

    except PageNotAnInteger :
        page = 1
    except EmptyPage:
        page = 1
    p = Paginator(courses_list,4,request=request)  #这一步以及把course_list传入了p,分页器

    courses = p.page(page) # 最终传入前端的是courses

    return render(request,'course-list.html',locals())


def course_detail(request,course_id):

    course = Course.objects.get(id=course_id)

    return render(request,'course-detail.html',locals())


from django.views.generic import DetailView

