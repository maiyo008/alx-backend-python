#!/usr/bin/python3
import sys
processing = __import__('1-batch_processing')

##### print processed users in a batch of 50
try:
    print(processing.batch_processing(50))
except BrokenPipeError:
    print('Broken pipe error')
    #sys.stderr.close()
