What is this?
--------------

*logs2json* is a simply python based utility which allows you to convert different log files into JSON format. 


Usage
-----------

    Usage: logs2json [options]
        To convert log to json

    options:
    -h/--help      to see help
    -f/--file      the file name
    -t/--type      the log type, now support: nginx/elb/csv
                    default value is nginx


Demo 
------------
    
     ./logs2json -t nginx -f data/nginxdata
     ./logs2json -t elb -f data/elbdata
     ./logs2json -t csv -f data/csvdata

