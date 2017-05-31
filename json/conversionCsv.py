import fileinput
import time
import csv
from common import *

def toEntity(file):

    csvfile = open(file, 'r')
    filecontent = []
    reader = csv.DictReader(csvfile)

    for row in reader : 
        rowFormat = toFormat(row)
        filecontent.append(rowFormat)

    return filecontent


def toFormat(res): 
    #oldTimeString = res['TIME'][0:-6]
    #timeObject = time.strptime(oldTimeString, "%d/%b/%Y:%H:%M:%S")
    #newTimeString = time.strftime("%Y-%m-%d %H:%M:%S", timeObject)
    #res['TIME'] = newTimeString
    return res
