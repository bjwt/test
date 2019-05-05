#coding=UTF-8
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib, time, re
#from xml.etree import ElementTree as ET
from xml.etree import ElementTree as ET
#from xml import etree
from django.utils.encoding import smart_str
import logging

log=logging.getLogger('test1')

def login_view(request):    
    if request.POST.has_key('username'):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)    
    #验证失败，暂时不做处理
    return  HttpResponseRedirect("/")

def logout_view(request):
    logout(request)
    return  HttpResponseRedirect("/")

@csrf_exempt
def weixin(request):
    if request.method=='GET':
        response=HttpResponse(checkSignature(request))
        log.info("check signature")
        return response
    else:
        log.info("POST")
        reply2 = """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[music]]></MsgType>
				<Music>
				<Title><![CDATA[从开始到现在]]></Title>
				<Description><![CDATA[歌手_张信哲]]></Description>
				<MusicUrl><![CDATA[http://123.57.55.200/zxz.mp3]]></MusicUrl>
				<HQMusicUrl><![CDATA[http://123.57.55.200/zxz.mp3]]></HQMusicUrl>
				</Music>
                </xml>"""

        reply = """<xml>
                <ToUserName><![CDATA[%s]]></ToUserName>
                <FromUserName><![CDATA[%s]]></FromUserName>
                <CreateTime>%s</CreateTime>
                <MsgType><![CDATA[news]]></MsgType>
                <ArticleCount>2</ArticleCount>
                <Articles>
                <item>
                <Title><![CDATA[芈月]]></Title> 
                <Description><![CDATA[史上第一个太后]]></Description>
                <PicUrl><![CDATA[http://52.77.210.85/static/2.png]]></PicUrl>
                <Url><![CDATA[http://restapi.amap.com/v3/staticmap?location=116.334831,40.040215&zoom=17&size=750*300&markers=mid,,A:116.334831,40.040215&key=e3cb09daaa47fb81fff57de497dee642]]></Url>
                </item>
                <item>
                <Title><![CDATA[芈姝]]></Title>
                <Description><![CDATA[楚国楚威后所生的嫡公主]]></Description>
                <PicUrl><![CDATA[http://52.77.210.85/static/30.png]]></PicUrl>
                <Url><![CDATA[http://baike.baidu.com/link?url=H0yeGbyIcqnaMEt7VeKa9sC2vi7rce7SXNJYVcuVHHCbk8A9OO-mlzgT2CdIcSQAi3TDo13B7e9bcf0150OhVtzRgM8qsGGBdWew6_1LjcO]]></Url>
                </item>
                </Articles>
                </xml>"""
        if request.body:
            log.info("body")
            xml_str = smart_str(request.body)
            log.info(xml_str)
            xml = ET.fromstring(request.body)
            content = xml.find("Content").text
            fromUserName = xml.find("ToUserName").text
            toUserName = xml.find("FromUserName").text
            postTime = str(int(time.time()))
            log.info(content)
            if not content:
                #return HttpResponse(reply % (toUserName, fromUserName, postTime, "输入点命令吧..."))
                return HttpResponse(reply % (toUserName, fromUserName, postTime))
            if content == "dianshi":
                #return HttpResponse(reply % (toUserName, fromUserName, postTime, "查询成绩绩点请到http://chajidian.sinaapp.com/ 本微信更多功能开发中..."))
                log.info(reply2)
                return HttpResponse(reply2 % (toUserName, fromUserName, postTime))
            else:
                log.info(reply)
                return HttpResponse(reply % (toUserName, fromUserName, postTime))
        else:
            return HttpResponse("Invalid Request")

def checkSignature(request):
    signature=request.GET.get('signature',None)
    timestamp=request.GET.get('timestamp',None)
    nonce=request.GET.get('nonce',None)
    echostr=request.GET.get('echostr',None)
    token="fedosu85"

    tmplist=[token,timestamp,nonce]
    tmplist.sort()
    tmpstr="%s%s%s"%tuple(tmplist)
    tmpstr=hashlib.sha1(tmpstr).hexdigest()
    if tmpstr==signature:
        return echostr
    else:
        return None
