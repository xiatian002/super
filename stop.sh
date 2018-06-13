#!/bin/bash
kill -9 `ps -ef|grep manage.py|grep -v grep |awk '{print $2}'`
process_id=`ps -ef|grep manage.py|grep -v grep|awk '{print $2}'`
if [ ! -n "${process_id}" ]; then
  echo "news_web is stoped"
else
  echo "news_web is still runing"
fi
