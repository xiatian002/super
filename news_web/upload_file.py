#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
import os,sys
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf

def upload_file(request):
    if request.method == "POST": 
        myFile = request.FILES.get("compress_file") #获取上传文件，如果没有文件就默认为None
        if not myFile:
            return HttpResponse("no file upload")
        destination = open(os.path.join("/opt/py/super/uploads/media/",myFile.name),"wb+")
        print("upload file destination is {}".format(destination))
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        resp = {}
        return HttpResponse(json.dumps(resp),content_type="application/json")
