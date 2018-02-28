# /usr/administrator/ python 27
# -*- coding: utf-8 -*-
# @Time    : 2018/1/29 16:38
# @Site    : 
# @File    : forms.py
# @Software: pycharm

from captcha.fields import CaptchaField
from django import forms


class RegisterForm(forms.Form):

    password = forms.CharField(label='密码',min_length=5,required=True)
    email = forms.EmailField(label='邮箱',required=True)
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})


class loginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, required=True)
    password = forms.CharField(label='密码', min_length=5, required=True)
















# from django import forms
# from rl_app.models import UserProfile
# from captcha.fields import CaptchaField
#
#
# class RegisterForm(forms.Form):
#     '''''
#     注册
#     '''
#     username = forms.EmailField(widget=forms.TextInput(
#         attrs={"class": "form-control", "placeholder": "请输入邮箱账号", "value": "", "required": "required", }),
#                                 max_length=50, error_messages={"required": "用户名不能为空", })
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={"class": "form-control", "placeholder": "请输入密码", "value": "", "required": "required", }),
#                                min_length=8, max_length=50, error_messages={"required": "密码不能为空", })
#     # 验证码
#     captcha = CaptchaField()
#
#     def clean(self):
#
#         # 验证码
#         try:
#             captcha_x = self.cleaned_data['captcha']
#         except Exception as e:
#             print
#             'except: ' + str(e)
#             raise forms.ValidationError(u"验证码有误，请重新输入")
#
#
#             # 用户名
#         try:
#             username = self.cleaned_data['username']
#         except Exception as e:
#             print
#             'except: ' + str(e)
#             raise forms.ValidationError(u"注册账号需为邮箱格式")
#
#
#             # 登录验证
#         is_email_exist = UserProfile.objects.filter(email=username).exists()
#         is_username_exist = UserProfile.objects.filter(username=username).exists()
#         if is_username_exist or is_email_exist:
#             raise forms.ValidationError(u"该账号已被注册")
#
#
#             # 密码
#         try:
#             password = self.cleaned_data['password']
#         except Exception as e:
#             print
#             'except: ' + str(e)
#             raise forms.ValidationError(u"请输入至少8位密码");
#
#         return self.cleaned_data

