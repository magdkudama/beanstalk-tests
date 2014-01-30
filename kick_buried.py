#!/usr/bin/env python
import beanstalkc

# Requirements: pip install beanstalkc && pip install pyyaml

beanstalk = beanstalkc.Connection()
beanstalk.watch('test-queue')
beanstalk.use('test-queue')
beanstalk.ignore('default')

beanstalk.kick()