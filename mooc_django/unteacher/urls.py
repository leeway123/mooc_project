"""unteacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
import xadmin
from django.conf import settings
from django.views.static import serve
from rl_app import views
from django.contrib import admin


urlpatterns = [
    url(r'^adminx/', xadmin.site.urls),
    # 首页

    url(r'^index/', views.index,name='index'),

    # 图片文件路径
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    url(r'^captcha/', include('captcha.urls')),

    # 教师版块
    url(r'^teacher/', include('teacher_app.urls', namespace='teacher')),
    url(r'^course/', include('course_app.urls',namespace='course')),

    # 登录注册
    url(r'^accounts/', include('rl_app.urls',namespace='accounts')),

    url(r'^active/(?P<active_code>.*)/$',views.ActiveUserView.as_view(),name='user_active'), # 激活码链接


]
