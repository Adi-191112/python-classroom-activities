import random
import time

def getRandomDate(startdate, endate):
    print("printing random dates between",startdate, "and",endate)
    randamgenarator = random.random()
    dateFormat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(startdate, dateFormat))
    endtime = time.mktime(time.strptime(endate, dateFormat))
    randomtime = starttime + randamgenarator * (endtime - starttime)
    randomdate = time.strftime(dateFormat, time.localtime(randomtime))
    return randomdate

print("randomdate = ", getRandomDate ('1/10/2016', '6/11/2017'))


