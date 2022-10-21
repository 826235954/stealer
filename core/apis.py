# Create your views here.
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.shortcuts import redirect, render

import core
from core.model import ErrorResult
from route import controller
from core.type import Video
import hashlib


def index(request):
    return render(request, 'index.html', {
        'items': Video.items_json()
    })


def ip(request):
    return redirect('http://httpbin.org/ip')


def fetch(request):
    itype = request.GET.get('type')
    if itype is None:
        return HttpResponseBadRequest(ErrorResult.TYPE_NOT_PRESENT.get_data())

    vtype = core.type.video_mapper.get(itype)
    if vtype is None:
        return HttpResponseServerError(ErrorResult.MAPPER_NOT_EXIST.get_data())

    return controller.fetch(vtype, request)


def download(request):
    itype = request.GET.get('type')  #  itype 是视频来源字符串，比如'auto'
    if itype is None:
        return HttpResponseBadRequest(ErrorResult.TYPE_NOT_PRESENT.get_data())

    vtype = core.type.video_mapper.get(itype) #  vtype 是视频来源字典，是Video类型（自定义的），比如<Video.AUTO: 'auto'>
    if vtype is None:
        return HttpResponseServerError(ErrorResult.MAPPER_NOT_EXIST.get_data())

    return controller.download(vtype, request)


def video_mapper(request):
    return HttpResponse(core.type.video_mapper_json)


def checkToken(request):
    try:
        signature = request.get("signature")  # 先获取加密签名
        timestamp = request.get("timestamp")  # 获取时间戳
        nonce = request.get("nonece")  # 获取随机数
        echostr = request.get("echostr") # 获取随机字符串
        token = "zyy" #自己设置的token

        # 使用字典序排序（按照字母或数字的大小顺序进行排序）
        list = [token, timestamp, nonce]
        list.sort()

        # 进行sha1加密
        temp = ''.join(list)
        sha1 = hashlib.sha1(temp.encode('utf-8'))
        hashcode = sha1.hexdigest()

        # 将加密后的字符串和signatrue对比，如果相同返回echostr,表示验证成功
        if hashcode == signature:
            return echostr
        else:
            return ""
    except Exception as e:
        return e