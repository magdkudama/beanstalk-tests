#!/usr/bin/env python
import beanstalkc

# Requirements: pip install beanstalkc && pip install pyyaml

def RESERVED():
    return "reserved"

beanstalk = beanstalkc.Connection()
beanstalk.watch('test-queue')
beanstalk.ignore('default')

beanstalkProducer = beanstalkc.Connection()
beanstalkProducer.watch('test-queue-producer')
beanstalkProducer.use('test-queue-producer')
beanstalkProducer.ignore('default')

def callback(data):
    print "Working..."
    return data

while True:
    job = beanstalk.reserve()
    if job is not None:
        if job.stats()['state'] == RESERVED():
            try:
                result = callback(job.body)
                beanstalkProducer.put(result)
                job.delete()
                print "Job " + job.body + " processed and deleted"
            except:
                print "Burying job " + job.body
                job.bury()
