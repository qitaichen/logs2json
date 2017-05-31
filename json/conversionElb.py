import fileinput
import re
import os
import time
from common import *

#read input file and return entries' Dict Object
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
                lineJson=line2dictElb(line)

                filecontent.append(lineJson)

        fileinput.close()
    return filecontent


#gets a line of string from Log and convert it into Dict Object
def line2dictElb(line):
    #Snippet, thanks to http://www.seehuhn.de/blog/52
    parts = [
    r'(?P<time>\S+)',            
    r'(?P<elb>\S+)',              
    r'(?P<client>\S+)',          
    r'(?P<backend>\S+)',          
    r'(?P<request_processing_time>\S+)', 
    r'(?P<backend_processing_time>\S+)',  
    r'(?P<response_processing_time>\S+)',  
    r'(?P<elb_status_code>\S+)',   
    r'(?P<backend_status_code>\S+)',
    r'(?P<received_bytes>\S+)', 
    r'(?P<sent_bytes>\S+)', 
    r'"(?P<method>\S+)',  
    r'(?P<url>\S+)',       
    r'(?P<protocal>\S+)"',     
    r'"(?P<user_agent>.*)"', 
    r'(?P<ssl_cipher>\S+)',       
    r'(?P<ssl_protocol>\S+)',       
]
    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
    m = pattern.match(line)
    res = m.groupdict()
    # url parse: file_name?xxx=yy&zz=tt
    newRes = toParseUrl(res, "url")
    formatRes = toFormatElb(newRes)

    return formatRes


def toFormatElb(res): 
    oldTimeString = res['time'][0:-8]
    timeObject = time.strptime(oldTimeString, "%Y-%m-%dT%H:%M:%S")
    newTimeString = time.strftime("%Y-%m-%d %H:%M:%S", timeObject)
    res['time_new'] = newTimeString
    return res
