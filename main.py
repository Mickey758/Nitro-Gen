import random
import time
import os
import threading

amt = 0
gen = 0

cap = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
low = list("abcdefghijklmnopqrstuvwxyz")
num = list("1234567890")    

def title():
    while 1: os.system("title {}/{}".format(gen,amt))
threading.Thread(target=title).start()

while 1:
    gen = 0
    amt = 0
    
    amt = int(input("Ammount Of Codes To Generate: "))
    file = open("nitro.txt","a",errors="ignore")
    a = time.time()
    while gen != amt:
          nitro = "https://discord.gg/{}\n".format("".join(random.choices(cap+low+num,k=16)))
          file.write(nitro)
          gen+=1
    b = time.time()
    file.close()

    print("Finished generating {} Codes In {} Seconds".format(amt,round(b-a,2)))
