# import socket programming library
import socket
import sys
import numpy
import os

## sudo service network-manager restart

#### Y-Position String Conversion to 2 Bytes Charset
# # Conversion
# length = 910
# message = 186
# ratio = message/length
#
# print("Length of Roller: ", length)
# print("Y-Position: ", message)
# print("Ratio: ", ratio)
#
# i = int((2**16-1)*ratio) # 16 bit int
# i.to_bytes(2, byteorder='big') # Bytes
# print("16 bit Int: ", i)
# output = (i).to_bytes(2, byteorder='big') # 2 Bytes
# print("2-Byte Output: ", output)


def Main():

    host = "192.168.0.101"  # Standard loopback interface address (localhost)
    port = 53985  # Port to listen on (non-privileged ports are > 1023)
    addr = ""

    # AF_NET is address family for IPv4
    #SOCK_STREAM is socket type for TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind((host, port))
    print("socket binded to port", port)
    s.listen()
    print("Socket is listening")

    try:
        while True:
            conn, addr = s.accept() # Call in while loop to keep accepting.
            #print('Connected to :', addr[0], ':', addr[1])
            data = conn.recv(2)
            print("Android Sent: " + str(data) + "  " + str(type(data)))
            if not data:
                print('No Data - Disconnected')
                break
            buffer = data
            conn.sendall(buffer)
            print("Return: " + str(buffer) + "  " + str(type(buffer)))

    except OSError:
        print("OS Error")
        pass

    print("Client Disconnected.")

if __name__ == '__main__':
    Main()
