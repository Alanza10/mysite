#!/bin/sh
cd /home/gelo/django/mysite
git push ssh://root@192.168.1.1/mnt/git/mysite
ssh pi@192.168.1.32 "deploydjango"
