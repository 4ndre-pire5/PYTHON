import time

timenow = time.localtime(time.time())
year, month, day, hour, minute, second = timenow[0:6]

print(str(day) + "/" + str(month) + "/" + str(year))
print(str(hour) + ":" + str(minute) + ":" + str(second))
print("\n")

now = time.gmtime()
print(now)
print("\n")

timeStr = time.asctime()
print(timeStr)


