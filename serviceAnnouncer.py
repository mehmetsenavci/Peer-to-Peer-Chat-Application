import socket
import json
import time



serviceAnn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
serviceAnn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serviceAnn.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# serviceAnn.settimeout(0.2)
# serviceAnn.bind(("", 5000))

username = input("Please enter your username: ")

message = {"username": username, "ip_address": socket.gethostbyname(socket.gethostname())}
jsonMessage = json.dumps(message).encode()

while True:
    print("Broadcasting the message.")
    serviceAnn.sendto(jsonMessage, ("<broadcast>", 5000))
    time.sleep(20)
    


