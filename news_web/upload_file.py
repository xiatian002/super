#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
import os,sys
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
import zipfile

def unzip_file(file_name):
    zip_file = zipfile.ZipFile(file_name)
    zip_file.extractall(path='/tmp/12345/')

def upload_file(request):
    if request.method == "POST": 
        myFile = request.FILES.get("compress_file") #获取上传文件，如果没有文件就默认为None
        if not myFile:
            return HttpResponse("no file upload")
        if(zipfile.is_zipfile("/opt/py/super/uploads/media/"+myFile.name)):
            destination = open(os.path.join("/opt/py/super/uploads/media/",myFile.name),"wb+")
            print("upload file destination is {}".format(destination))
            for chunk in myFile.chunks():
                destination.write(chunk)
            destination.close()
            unzip_file(destination.name)
            resp = {'result_code':'0','content':'upload sucessed'}
            return HttpResponse(json.dumps(resp),content_type="application/json")
            print("upload file is a zip file")
        else:
            resp = 'upload file is not a zip file'
            #return HttpResponse(json.dumps(resp),content_type="application/json")
            return HttpResponse(resp)
