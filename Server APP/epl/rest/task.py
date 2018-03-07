#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 16:01:38 2018

@author: johnkenny
"""

from celery.task.schedules import crontab
from celery.decorators import task

# this will run every minute, see http://celeryproject.org/docs/reference/celery.task.schedules.html#celery.task.schedules.crontab
@task(run_every=crontab(hour="*", minute="1", day_of_week="3"))
def test():
    print "firing test task"