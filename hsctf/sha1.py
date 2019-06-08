
import hashlib


f = open('/usr/share/wordlists/rockyou.txt', 'rb')
for z in f:
    d = z.replace("\n","")
    #print d
    s = hashlib.sha1(d).hexdigest()
    #print d
    if "0ce7911e6479995d6c346d6f03eb723b5135309e" == s:
        print "flag is" , d
