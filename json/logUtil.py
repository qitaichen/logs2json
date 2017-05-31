import sys
try: import simplejson as json
except ImportError: import json

import conversionNginx
import conversionElb
import conversionCsv

#to get jSon of entire Log
#returns JSON object
def toJson(file, type):
    #get dict object for each entry
   
    entities = []
    if type == "nginx": 
        entities = conversionNginx.toEntity(file)
    elif type == "elb":
        entities = conversionElb.toEntity(file)
    elif type == "csv":
        entities = conversionCsv.toEntity(file)
    else : 
        print("Invalid type:%s" % type)
        sys.exit(2)

    outputString = ""
    for line in entities: 
        outputString += json.JSONEncoder().encode(line) + "\n"

    return outputString

