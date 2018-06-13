#!/bin/bash
#startup helloworld django project
#nohup python3 manage.py runserver 0.0.0.0:8000 &
file_date=`date +%Y-%m-%d`
nohup python3 manage.py runserver 0.0.0.0:8000 >> ./logs/${file_date}.logs 2>&1 &
#sleep 12
process_id=`ps -ef|grep manage.py|grep -v grep|awk '{print $2}'`
process_port=`netstat -anp|grep 8000|awk '{print $6}'`
if [ ! -n "${process_id}" ]; then
  echo "error start news_web failed"
#elif [ ${process_port} == "LISTEN" ]; then
#  echo "news_web is running"
fi
echo "server start successfully"
