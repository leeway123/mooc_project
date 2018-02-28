# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from captcha.fields import CaptchaField
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    username = models.CharField(max_length=20,verbose_name='用户名',unique=True)
    img = models.ImageField(upload_to='user/%Y/%m', max_length=200, blank=True, null=True, verbose_name='用户头像')
    password = models.CharField(max_length=100,verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    is_active = models.BooleanField(default=False,verbose_name='是否激活')
    sex = models.CharField(max_length=10,verbose_name='性别')
    captcha = CaptchaField(error_messages={"invalid": "验证码错误"})



    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # 包含注册验证和找回验证
    send_type = models.CharField(verbose_name=u"验证码类型", max_length=10, choices=(("register",u"注册"), ("forget",u"找回密码")))
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)
    class Meta:

        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name
    def __str__(self):

        return '{0}({1})'.format(self.code, self.email)
