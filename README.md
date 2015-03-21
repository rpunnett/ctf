proxy_injection_test
=========

A Python script to check if a proxy is injecting JS or HTML. Verifies MD5 hashes of jQuery and Space Jam website to check for tampering. 

Usage
----

Call the script with the requested arguments:

t = Protocol: http or https
i = IP or Hostname
p = Port


        python proxyTest.py t "http" i "120.198.243.54 p "80" 


License
----

MIT
