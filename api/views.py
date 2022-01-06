from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from django_redis import get_redis_connection
from .serializer.account import LoginSerializer,MessageSerializer

import random
import uuid
from api import models
from utils.tencent.sms import send_message



class LoginView(APIView):

    def post(self,request,*args,**kwargs):
        print(request.data)
        '''
        1，校验手机号
        2，校验验证码，redis
        3，去数据库中获取用户信息（获取/创建)
        4，返回信息
        '''
        ser = LoginSerializer(data=request.data)
        if not ser.is_valid():
            return Response({"status": False,"message":"验证码错误"})
        phone = ser.validated_data.get('phone')
        user_object,flag = models.UserInfo.objects.get_or_create(phone=phone)
        user_object.token = str(uuid.uuid4())
        user_object.save()
        return Response({"status":True,"userinfo":{"phone":phone,"token":user_object.token}})

class MessageView(APIView):
    def get(self,request,*args,**kwargs):
        '''
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 1，获取手机号
        # 2，手机格式校验
        # import re
        # if not re.match(r'^(1[3|4|5|6|7|8|9])\d{9}$',phone):
        #     print("手机号格式错误")
        #     return Response({"status": False,"msg":"手机号格式错误"})
        ser = MessageSerializer(data=request.query_params)
        if not ser.is_valid():
            return Response({"status": False,"massage":"手机号格式错误"})
        phone = ser.validated_data.get("phone")
        # 3，生成验证码
        random_code = random.randint(1000,9999)
        '''
        # 4，发送短信。购买短信服务，阿里云，腾讯云
        result = send_message(phone,random_code)
        if not result:
            return Response({"status": False,"message":"短信发送失败"})
        '''
        print(random_code)
        # 5，保留手机号和验证码，设置失效时间60秒。django-redis
        # 5.1配置
        # 5.2使用
        conn = get_redis_connection()
        conn.set(phone,random_code,ex=60)

        return Response({"status": True,"message":"发送成功"})
