import requests
from Crypto.Hash import MD4

host = "https://md4.web.chal.hsctf.com/?md4="

#s = request.sessions()

q = requests.get(host)
s = q.content



for x in str(range(0,10000)):
    h = MD4.new(x)
    g = h.hexdigest()
    sdf = host + str(g)
 #   print sdf
    fgh = requests.get(sdf)
    if "ctf" in fgh:
        print "hai",fgh


        
