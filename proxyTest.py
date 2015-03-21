#!/usr/bin/python

def main():
   
   import urllib2
   import hashlib
   import argparse

   parser = argparse.ArgumentParser(description="""Verifies MD5 of a JS and HTML
                                                File and checks for code
                                                injection by a proxy""")
   parser.add_argument('type', metavar='t', type=str, nargs='+',
                      help='The communication protocol: http or https')
   parser.add_argument('ip', metavar='i', type=str, nargs='+',
                      help='The IP or hostname of the proxy')
   parser.add_argument('port', metavar='p', type=str, nargs='+',
                      help='The Port of the proxy')

   args = parser.parse_args()
               

   html_url = "http://www2.warnerbros.com/spacejam/movie/jam.htm"
   html_md5Verification = "14773a0103077af1bcd55713ed284ef2"
   js_url = "http://code.jquery.com/jquery-1.11.2.min.js"
   js_md5Verification = "5790ead7ad3ba27397aedfa3d263b867"
   
   proxy_protocol = str(args.type)
   proxy_ip = str(args.ip)
   proxy_port = str(args.port)
   proxy_url = proxy_protocol + "://" + proxy_ip + ":" + proxy_port

   try:
      proxy_support = urllib2.ProxyHandler({proxy_protocol:proxy_url})
      opener = urllib2.build_opener(proxy_support)
      urllib2.install_opener(opener)
   except IOError:
       print "Connection error! (Check proxy)"
   else:
       print "Connected to Proxy"
       
   #Verify JS
   try:
       html = urllib2.urlopen(js_url).read()
   except urllib2.HTTPError:
       print "Connection error! (Check proxy)"
   else:
       print "Connected to JS CDN"

   m = hashlib.md5()
   m.update(html)

   if m.hexdigest() == js_md5Verification:
      print "JS is Secure"
   else:
      print "Tampering Found"

   #Verify HTML
   try:
       html = urllib2.urlopen(html_url).read()
   except urllib2.HTTPError:
       print "Connection error! (Check proxy)"
   else:
       print "Connected to SpaceJam HTML"

   m = hashlib.md5()
   m.update(html)

   if m.hexdigest() == html_md5Verification:
      print "HTML is Secure"
   else:
      print "Tampering Found"


   # end of proxyTest.py

if __name__ == "__main__":
    main()
