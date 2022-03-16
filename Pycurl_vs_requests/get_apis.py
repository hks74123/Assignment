# Pycurl vs python requests
"""

To compare better performance between these two we have fetch same api using these two methods and 
then compare timings.

"""
import time
import requests
import pycurl
import certifi
from io import BytesIO

# initializing time for request
request_time = 0

# initializing time fo pycurl
pycurl_time=0

# getting api using pycurl
def pycurl_get():
    b = BytesIO()
    c = pycurl.Curl()
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(c.URL, 'https://www.quora.com')
    c.setopt(c.WRITEDATA, b)
    c.perform()
    c.close()
    body = b.getvalue()
    print('pycurl_get: %s' % body.decode('utf8'))

# getting api using requests
def requests_get():
    r = requests.get('https://www.quora.com')
    print('requests_get: %s' % r.text)

# testing_api_for_less_no_of_time
def test_for_less_no_of_times():
    # start time of fetching api
    start_time = time.time()
    for i in range(10):
        requests_get()
    # end time which is after fetching 100 apis
    end_time = time.time()
    request_time = end_time - start_time

    start_time = time.time()
    for i in range(10):
        pycurl_get()
    end_time = time.time()
    pycurl_time = end_time - start_time

def test_for_more_no_of_times():
    # start time of fetching api
    start_time = time.time()
    for i in range(100):
        requests_get()
    # end time which is after fetching 100 apis
    end_time = time.time()
    request_time = end_time - start_time

    start_time = time.time()
    for i in range(100):
        pycurl_get()
    end_time = time.time()
    pycurl_time = end_time - start_time

# printing the timings of both for less no. of api fetching time
test_for_less_no_of_times()
print('The timing of request is %f' % request_time)
print('The timing of pycurl is %f' % pycurl_time)

# printing the timings of both for more no. of api fetching time
test_for_more_no_of_times()
print('The timing of request is %f' % request_time)
print('The timing of pycurl is %f' % pycurl_time)
  
