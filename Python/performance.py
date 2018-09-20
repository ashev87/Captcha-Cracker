from os import walk
import timeit
import os
from PIL import Image
from algorithm import parser

f = []
for (dirpath, dirnames, filenames) in walk('preprocessing/download/'):
    f.extend(filenames)
    break
timesum = 0
size = len(f)
count = 1
maxtime = 0
mintime = 100
currtime = 0
for im in f:
    img = Image.open("preprocessing/download/"+str(im))
    starttime = timeit.default_timer()
    captcha = parser.parse_captcha(img)
    print("CAPTCHA:"+captcha)
    endtime = timeit.default_timer()
    currtime = endtime-starttime
    if(currtime > maxtime):
        maxtime = currtime
        maximg = img.copy()
        print("new max:"+str(maxtime))
    if(currtime < mintime):
        mintime = currtime
        minimg = img.copy()
        print("new min:"+str(mintime))

    timesum += currtime
    print("Comparing image "+str(count)+"/"+str(size))
    count += 1
avg = timesum/size

print("========================================")
print("Maximum Time:"+str(maxtime))
print("Minimum Time:"+str(mintime))
print("Total Time:"+str(timesum))
print("Average Time:"+str(avg))
print("========================================")
