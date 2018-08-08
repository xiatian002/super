#!/usr/local/bin/python3
#-*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import dns,dns.update,dns.query
import sys


#def update_domain(domain,domain_rrset,domain_addr,zone,server):#有默认值的参数放在最右边
def update_domain(request):#有默认值的参数放在最右边
    
    domain=request.GET['domain']
    domain_rrset=request.GET['domain_rrset']
    domain_addr=request.GET['domain_addr']
    zone=request.GET['zone']
    server=request.GET['server']

    update_obj=dns.update.Update(zone)
    update_obj.add(domain,3600,domain_rrset,domain_addr)#创建一个dns message
    result_code=dns.query.tcp(update_obj,server,timeout=10)#使用query 将dns message发送到指定的dns server
    return HttpResponse("result is {}".format(result_code.rcode()))
    print("result is {}".format(result_code.rcode()))

#if __name__ == '__main__':
#    domain=sys.argv[1]
#    domain_rrset=sys.argv[2]
#    domain_addr=sys.argv[3]
#    zone = sys.argv[4]
#    server = sys.argv[5]
#    update_domain(domain,domain_rrset,domain_addr,zone,server)
