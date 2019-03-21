import sys
import string
import time
from threading import Thread
import random
import os

chara = []
diff = str(input("Mudah / Normal / Sulit / Gila: "))


null = 0

if diff.startswith("M"):
    for aaa in list(string.ascii_lowercase):
        chara.append(aaa)
        
        
if diff.startswith("N"):
    for aaa in list(string.ascii_lowercase):
        chara.append(aaa)
    for aaa in list(string.ascii_uppercase):
        chara.append(aaa)

if diff.startswith("S"):
    for aaa in list(string.ascii_lowercase):
        chara.append(aaa)
    for aaa in list(string.ascii_uppercase):
        chara.append(aaa)
    for aaa in list(string.digits):
        chara.append(aaa)

if diff.startswith("G"):
    for aaa in list(string.ascii_lowercase):
        chara.append(aaa)
    for aaa in list(string.ascii_uppercase):
        chara.append(aaa)
    for aaa in list(string.digits):
        chara.append(aaa)
    for aaa in ["[", "]", "/", "\\", "+", "-", "_", ";", ":", "'", '"', "<", ">", "?"]:
        chara.append(aaa)

berapa = int(input("mau berapa karakter? "))
waktu = int(input("berapa detik? "))

ready = []


for bca in range(berapa):
    oke = random.choice(chara)
    ready.append(oke)
    
    



null = 0
jadi = ""
for cab in ready:
    if null == 4:
        jadi += " "
        null = 0
    jadi += cab
    null += 1

stop = 0
jawab = ""



os.system("clear")
print("PERMAINAN AKAN DIMULAI DALAM\n\n")
if True:
    print("5", end="\r")
    time.sleep(1)
    print("4", end="\r")
    time.sleep(1)
    print("3", end="\r")
    time.sleep(1)
    print("2", end="\r")
    time.sleep(1)
    print("1", end="\r")
    time.sleep(1)
    print("    ", end ="\r")
print("\n")    
print(jadi)
print("\n")


jawab = None
def check():
    salah = 0
    null = 0
    time.sleep(waktu)
    for benar in jadi:
        try:
            if benar != jawab[null]:
                salah += 1
                null += 1
        except:
            salah += 1
            null += 1
    print("\nsalahmu ada: %d\n" %(salah))
    print(jawab)
    print("waktu habis") 
Thread(target=check, args=[]).start()
jawab = str(input("kata: "))