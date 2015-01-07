#!/usr/bin/python

import urllib2
import hashlib
#46.10.14.206:1080
#213.231.161.111:10045
proxy_type = "http"
proxy_ip = "190.198.144.127"
proxy_port = "8080"

proxy_url = proxy_type + "://" + proxy_ip + ":" +proxy_port

js_url = "http://code.jquery.com/jquery-1.11.2.min.js"
md5Verification = "5790ead7ad3ba27397aedfa3d263b867"

try:
   proxy_support = urllib2.ProxyHandler({proxy_type:proxy_url})
   opener = urllib2.build_opener(proxy_support)
   urllib2.install_opener(opener)
except IOError:
    print "Connection error! (Check proxy)"
else:
    print "Connected to Proxy"

try:
    html = urllib2.urlopen(js_url).read()
except urllib2.HTTPError:
    print "Connection error! (Check proxy)"
else:
    print "Connected to JS CDN"


m = hashlib.md5()
m.update(html)

if m.hexdigest() == md5Verification:
   print "JS is Secure"
else:
   print "Tampering Found"




#print html

# end of proxyTest.py
