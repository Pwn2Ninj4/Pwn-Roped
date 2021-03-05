#!/usr/bin/python3
import sys
import os
import argparse


#colors and fronts
"""fonts"""
normal = '\033[0m'
bold = '\033[1m' 
dim = '\033[2m'
italic = '\033[3m' 
under = '\033[4m'
blink = '\033[5m'
reverse = '\033[7m'
conceal = '\033[8m'
nobold = '\033[22m'
noitalic = '\033[23m'
nounder = '\033[24m'
noblink = '\033[35m'
"""Colors(Foreground)"""
gray = '\033[1;30m'
red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
white = '\033[1;37m'


def main():
    if len(sys.argv)<3:
        print("{}\t\t!Pwn-Roped.py: {}ROP{} Xploit's Generator\n{}[+]{}By Pwn2Ninja".format(gray, red, blue, red, blue))
        print("\n{}Usage: {}python3{} Pwn-Roped.py {}<binary> <libc>{}".format(gray, blue, blue, red, white))
    else:
        binary = sys.argv[1]
        libc = sys.argv[2]
        xploit = '''#!/usr/bin/python3
from pwn import *

elf = ELF("./{}")

#Descomenta estas líneas dependiendo del binario
#p = remote("host", 1234)
#p = elf.process()

#=================exploit here===============
rop = ROP(elf)
rop.call(elf.symbols)#continue aquí el exploit
rop.call(elf.symbols)#continue aquí el exploit



payload = [

] #continue aquí el exploit
payload = #continue aqui el exploit

libc = ELF("{}")
rop = ROP(libc)
rop.call()#continue aqui el exploit
rop.call()#continue aquí el exploit
rop.call()#continue aquí el exploit

payload = [

]#continue aquí el exploit
payload = #continue aquí el exploit

p.sendline(payload)

#=================interactive==================
p.interactive()
    '''.format(binary, libc)
        try:
            with open('xploit.py', 'w') as xpl:
                xpl.write(xploit)
                xpl.close()
                print("{}[+]{}Xploit created succefully{}".format(red, blue, white))
        except:
            print("{}[!]{}Can't write the xploit{}".format(red, blue, white))
        
if __name__ == '__main__':
    main()