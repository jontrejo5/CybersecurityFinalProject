import os
import socket

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

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    for x in range(startport,endport):
        result = sock.connect_ex((hostname, x))
        if result == 0:
            stringresult += str("Port "+ str(x) + " is open\n")
        else:
            stringresult += str("Port "+ str(x) + "  is not open\n")


    return stringresult