import datetime
t = datetime.time(22,57,44,23)
print(t)
print("Hour : ",t.hour)
print("Minute : ",t.minute)
print("Second : ",t.second)
print("Micro Second : ",t.microsecond)

print("----------------------------------------------")

d = datetime.date.today()
print(d)
print(" Year : ",d.year)
print("Month : ",d.month)
print("Day : ",d.day)

print("----------------------------------------------")
d1 = datetime.date.today()
print(d1)
td = datetime.timedelta(days=2)
print(td)
d2=d1+td
print(d2)


dt=datetime.datetime.combine(d,t)
print(dt)