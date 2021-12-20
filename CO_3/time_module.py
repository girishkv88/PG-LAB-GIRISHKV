import time
print("Current time in sec :",time.time())

print("Current time :",time.ctime())

print("Current time after 30 sec :",time.ctime(time.time()+30))

t = time.localtime()
print("Time : ",t)
print("Current Year : ",t.tm_year)
print("Current Month : ",t.tm_mon)
print("Current Day : ",t.tm_mday)
print("Current Hour : ",t.tm_hour)
print("Current Minute : ",t.tm_min)
print("Current Second : ",t.tm_sec)
print("Current Weakday : ",t.tm_wday)
print("Current YearDay : ",t.tm_yday)









