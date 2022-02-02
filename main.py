#!/usr/bin/python3
import ipv4pool
import requester
import dbconnector
import time

sleeptime = 4

print("curip = ", end='')
curip = input()
print("endip = ", end='')
endip = input()

ipv4pool = ipv4pool.IPv4Pool(curip, endip)
db = dbconnector.RemoteDB("hostname", 3306, "username", "password", "database")

stopflag = False
ippool = []
while True:
    for i in range(100):
        ippool.append(ipv4pool.get())
        if not ipv4pool.next256():
            stopflag = True
            break
    while True:
        try:
            db.new(requester.batch(ippool))
        except:
            continue
        print(ippool)
        ippool.clear()
        break
    if stopflag:
        break
    time.sleep(sleeptime)
