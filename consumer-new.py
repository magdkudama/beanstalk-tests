#!/usr/bin/env python
import beanstalkc

beanstalk = beanstalkc.Connection()
beanstalk.watch('test-queue-producer')
beanstalk.ignore('default')

def RESERVED():
    return "reserved"

def callback(data):
    print "Working..."
    return data

while True:
    job = beanstalk.reserve()
    if job is not None:
        if job.stats()['state'] == RESERVED():
            try:
                callback(job.body)
                print "Job " + job.body + " processed and deleted"
            except:
                print "Burying job " + job.body
                job.bury()
