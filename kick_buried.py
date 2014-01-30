#!/usr/bin/env python
import beanstalkc

# Requirements: pip install beanstalkc && pip install pyyaml

beanstalk = beanstalkc.Connection()
beanstalk.watch('player-model.sessions')
beanstalk.use('player-model.sessions')
beanstalk.ignore('default')

beanstalk.kick()