# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Teacher(models.Model): # 教师信息表
    name = models.CharField(max_length=20,verbose_name='教师姓名')
    age = models.IntegerField(verbose_name='年龄')
    photo = models.ImageField(upload_to='teacher/%Y/%m', max_length=200, blank=True, null=True, verbose_name='用户头像')
    is_admit = models.BooleanField(max_length=1,choices=((0,'是'),(1,'否')),default=1,verbose_name='是否认证')
    work_time = models.IntegerField(verbose_name='工作年限')
    company = models.CharField(max_length=50,verbose_name='就职公司')
    job = models.CharField(max_length=50,verbose_name='工作职位')
    character = models.CharField(max_length=200,verbose_name='教学特点')
    visit_num = models.IntegerField(default=0,verbose_name='浏览人数')
    is_collect = models.BooleanField(max_length=1, choices=((0, '是'), (1, '否')), default=1, verbose_name='是否收藏')
    sex = models.CharField(max_length=10,default='男',verbose_name='性别')

    class Meta:

        verbose_name = '教师表'
        verbose_name_plural = verbose_name


    # 通过外键，查询老师对应的课程

    def querry_course(self):
        return self.course_set.all()




    def __str__(self):
        return  self.name


class Course(models.Model): # 课程表
    teacher = models.ForeignKey(Teacher, blank=True, null=True, verbose_name='教师姓名')
    name = models.CharField(max_length=50,verbose_name='课程名字')
    photo = models.ImageField(upload_to='course/%Y/%m',max_length=200, blank=True, null=True, verbose_name='课程封面')
    time =models.IntegerField(default=0,verbose_name='课程时长')
    student_count = models.IntegerField(verbose_name='学习人数')
    is_collect = models.BooleanField(max_length=1, choices=((0, '是'), (1, '否')), default=1, verbose_name='是否收藏')
    level = models.CharField(max_length=10,default='入门',verbose_name='课程难度')
    lesson_num = models.IntegerField(default=0,verbose_name='课程章节数')
    has_fav = models.IntegerField(default=0,verbose_name='收藏人数')



    class Meta:
        verbose_name = '课程列表'
        verbose_name_plural = verbose_name



    def __str__(self):
        return  self.name

class Lessones(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')







