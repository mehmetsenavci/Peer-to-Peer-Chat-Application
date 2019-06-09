import socket
import json


onlineUsers = dict()
REVonlineUsers = dict()


serviceListner = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serviceListner.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serviceListner.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
serviceListner.bind(("", 5000))

while True:
    message, address = serviceListner.recvfrom(1024)
    parsedMessage = json.loads(message)
    #print(parsedMessage)
    #print(address[0])
    #print(len(onlineUsers))

    if len(onlineUsers) != 0:
        if address[0] not in list(onlineUsers.values()):
            onlineUsers[parsedMessage["username"]] = address[0]
            REVonlineUsers[address[0]] = parsedMessage["username"]
            #print(list(onlineUsers.values()))
            print(REVonlineUsers[address[0]] + " is online now.")
            with open("Users.txt", mode="w", encoding="utf-8") as users:
                for username, ip in onlineUsers.items():
                    users.write(username + "," + ip + "\n" )
            

    else:
        onlineUsers[parsedMessage["username"]] = address[0]
        REVonlineUsers[address[0]] = parsedMessage["username"]
        print(REVonlineUsers[address[0]] + " is online now.")
        with open("Users.txt", mode="w", encoding="utf-8") as users:
            for username, ip in onlineUsers.items():
                users.write(username + "," + ip + "\n" )
    
    #print(REVonlineUsers)
    


