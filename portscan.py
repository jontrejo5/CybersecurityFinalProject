import os
import socket
import json
import pprint

#print("Jonathan,  python port scanner")

# input vars

#hostname, startport, endport = input("Enter IP addr, startpoint, endpoint (127.0.0.0 1111 2222)").split()



def runportscan(hostname, startport, endport):

    startport = int(startport)
    endport = int(endport)



    # reply = os.system("pint -c 1 " + hostname)
    # if reply == 0:
    #     pingstatus = "active"
    # else:
    #     pingstatus = "error"

    stringresult = ""

    # file location
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    filename = 'ports.json'

    #socket setup
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for x in range(startport,endport):
        result = sock.connect_ex((hostname, x))
        if result == 0:
            stringresult += str("Port "+ str(x) + " is open\n")
            with open(fileDir+"/json/ports.json") as f:
                data = json.load(f)

                stringresult += str(data.get("ports").get(str(x)).get("description"))




    return stringresult