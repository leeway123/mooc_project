from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.generic import View
from datetime import datetime
from rl_app.forms import loginForm, RegisterForm
from rl_app.models import UserProfile, EmailVerifyRecord
from rl_app.utils.email_send import send_email


# from captcha import

# Create your views here.
def index(request):
    return render_to_response('index.html')

# class ActiveUserView(View): # 激活码
#     def get(self, request, active_code):
#         all_records = EmailVerifyRecord.objects.filter(code=active_code) # 获取匹配的激活码
#         if all_records: # 如果存在
#             for record in all_records:
#
#                 # 判断链接的时效性
#                 send_time = record.send_time
#                 current_time = datetime.now()
#                 time_difference = current_time - send_time
#                 if (time_difference.seconds // 60) <= 60:
#                     email = record.email
#                     user = UserProfile.objects.get(email=email)
#                     user.is_active = True # 激活，存入数据库
#                     user.save()
#                 else: # 如果失效，删除
#                     email = record.email
#                     UserProfile.objects.filter(email=email).delete()
#                     return render(request, "404.html")
#         else:
#             return render(request, "403.html")
        # return HttpResponse('注册成功')


class registerView(View):
    def get(self,request):
        regist_form = RegisterForm()
        return render(request,'register.html',locals())


    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("email", "")
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {"register_form": register_form, "msg": "用户已经存在"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_email(user_name, 'register')
            return render(request, "login.html",locals())
        else:
            return render(request, "register.html", {"register_form": register_form})


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = loginForm(request.POST) # 递的是 username和password
        if login_form.is_valid():# 进行判断是否符合LoginForm中定义的条件
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request,'login.html',{"login_form": login_form,'msg': u'用户未激活'})
            else:
                return render(request, "login.html", {"login_form": login_form, "msg": u"用户名或密码错误!"})
        else:
            return render(request, "login.html", {"login_form": login_form})



def log_out(request):
    logout(request)
    return render(request,'index.html',locals())



class ActiveUserView(View):
    def get(self, request, active_code):
    # 用code在数据库中过滤处信息
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                # 通过邮箱查找到对应的用户
                user = UserProfile.objects.get(email=email)
                # 激活用户
                user.is_active = True
                user.save()
        else:
            return render(request, "404.html")
        return render(request, "login.html")
