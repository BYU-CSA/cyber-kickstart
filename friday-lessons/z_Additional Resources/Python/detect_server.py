import requests, sys

servers = {}

# read in hosts file
if len(sys.argv) != 2:
    print("Usage: python3 detect_server.py /path/to/hostfile.txt")
    quit()
hosts = open(sys.argv[1], "r").read().splitlines()

# get Server for each page
for host in hosts:
    URL = "http://"+host+"/"
    
    try:
        # get response
        response = requests.request("GET", URL, timeout=4)
        headers = response.headers

        # collect Server header if present
        if 'Server' in headers:
            print(host+","+response.headers['Server'])
        else:
            print(host+",Unknown")

    except requests.exceptions.RequestException as e:
        # hostname doesn't exist, so skip
        ""