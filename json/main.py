import sys
import getopt
import os
from logUtil import *

def usage():
    print "Usage: logs2json [options]"
    print "    To convert log to json "
    print ""
    print "options:"
    print "  -h/--help      to see help"
    print "  -f/--file      the file name"
    print "  -t/--type      the log type, now support: nginx/elb/csv"
    print "                 default value is nginx"
    print ""


try: 
    options, args = getopt.getopt(sys.argv[1:], "hf:t:", ["help", "file=", "type"])
except getopt.GetoptError:
    usage()
    sys.exit()


file=""
type="nginx"
for name, value in options: 
    if name in ("-h", "--help"): 
        usage()
        sys.exit()
    if name in ("-f", "--file"): 
        file=value
    if name in ("-t", "--type"): 
        type=value
    
if file == '' : 
    print "File  is required"
    sys.exit(2)

if os.path.isfile(file) == False:
    print("file:%s is not exists" % file)
    sys.exit(2)


if type not in ["nginx", "elb", "csv"]: 
    print("Invalid type:%s" % type)
    sys.exit(2)

print (toJson(file, type))

