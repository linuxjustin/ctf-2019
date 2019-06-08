import hashlib

h = hashlib.new('md4',num).hexdigest()

#h = MD4.new()

string = "0e"
num = 0


while True:
    num = num + 1
    incr = str(num)
    test = h.update(string + incr)
    comp = str(test)
    hashed = str(h.hexdigest()).split("0e")
    if hashed[0] == "" and len(hashed) == 1:
        print("testing number : ", hashed[1])
        try:
            if int(hashed[1]):
                print("try : ", h.hexdigest())
                if int(hashed[1]) == num:
                    print("best solution found : ", h.hexdigest())
                break

        except:
            pass

    #print("testing number : ", h.hexdigest())
    #if
    #str(h.hexdigest()).split("0e")[0] == ""
    #break
    #if str(h.hexdigest()).split("0e")[0] == "" and str(h.hexdigest()).split("0e")[2] != '':
    #    if 
    #    print(string + incr)
    #    break

while True:
    num = num + 1
    val = str(num)
    h.update(val)
    print(h.hexdigest())
