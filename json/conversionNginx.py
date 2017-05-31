import fileinput
import re
import os
import time
from common import *

def toEntity(file):
    filecontent = []
    index = 0
    #check necessary file size checking
    statinfo = os.stat(file)

    #just a guestimate. I believe a single entry contains atleast 150 chars
    if statinfo.st_size < 15:
        print ("Not a valid access_log file. It does not have enough data")
    else:
        for line in fileinput.input(file):
            index = index+1
            if line != "\n": #don't read newlines
                lineJson=""
                lineJson=line2dictNginx(line)
                filecontent.append(lineJson)

        fileinput.close()
    return filecontent

#gets a line of string from Log and convert it into Dict Object
def line2dictNginx(line):
    #Snippet, thanks to http://www.seehuhn.de/blog/52
    parts = [
    r'(?P<HOST>\S+)',                   # host %h
    r'(?P<IDENTITY>\S+)',               # indent %l (unused)
    r'(?P<USER>\S+)',                   # user %u
    r'\[(?P<TIME>.+)\]',                # time %t
    r'"(?P<METHOD>\S+)',                # method "%r"
    r'(?P<URL>\S+)',                    # url "%r"
    r'(?P<PROTOCAL>\S+)"',              # protocal "%r"
    r'(?P<STATUS>[0-9]+)',              # status %>s
    r'(?P<SIZE>\S+)',                   # size %b (careful, can be '-')
    r'"(?P<REFERER>.*)"',               # referer "%{Referer}i"
    r'"(?P<USERAGENT>.*)"',                 # user agent "%{User-agent}i"
]
    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
    m = pattern.match(line)
    res = m.groupdict()
    # url parse: file_name?xxx=yy&zz=tt
    newRes = toParseUrl(res, "URL")
    formatRes = toFormatNginx(newRes)

    return formatRes


def toFormatNginx(res): 
    oldTimeString = res['TIME'][0:-6]
    timeObject = time.strptime(oldTimeString, "%d/%b/%Y:%H:%M:%S")
    newTimeString = time.strftime("%Y-%m-%d %H:%M:%S", timeObject)
    res['TIME'] = newTimeString
    return res
