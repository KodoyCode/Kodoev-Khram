import time

#Time in seconds

sec=time.time()
print('Time in seconds ', sec)

#Sleep

print('Sleeping...')
time.sleep(2)
print('Wake up, Mister Freeman, wake up and smell the ashes..')

#ctime

print(time.ctime())

#localtime

tim=time.localtime()
print(tim)
print(tim.tm_mon)
print(tim.tm_mday)
print(tim.tm_wday)
print(tim.tm_hour)
print(tim.tm_min)
print(tim.tm_sec)
