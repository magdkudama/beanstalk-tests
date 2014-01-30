#!/usr/bin/env python
import beanstalkc

# Requirements: pip install beanstalkc && pip install pyyaml

def RESERVED():
    return "reserved"

beanstalk = beanstalkc.Connection()
beanstalk.watch('test-queue')
beanstalk.ignore('default')

def callback(sessionId):
    print "Working..."

while True:
    job = beanstalk.reserve()
    if job is not None:
        if job.stats()['state'] == RESERVED():
            try:
                callback(job.body)
                job.delete()
                print "Job " + job.body + " processed and deleted"
            except:
                print "Burying job " + job.body
                job.bury()
