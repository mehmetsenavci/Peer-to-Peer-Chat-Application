import socket
import time
import datetime

usersAsList = list()
usersAsDict = dict()

with open("Users.txt", "r+", encoding="utf-8") as users:
    lines = users.readlines()
    for line in lines:
        line = line.strip("\n")
        usersAsList.append(line.split(","))

print("-----ONLINE USERS-----")
for name, ip in usersAsList:
    usersAsDict[name] = ip
    print(name)

while True:

    connectionUsername = input("Please enter the username of the user that you want to chat with...\n")
    connectionIP = usersAsDict[connectionUsername]


    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((connectionIP, 5001))

    timestamp = time.time()
    currTime = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    print("Please type quit to terminate the program")

    while(True):

        message = input("Enter the your message please: ").encode()

        if message.decode() == "quit":
            clientSocket.close()
            break

        else:
            timestamp = time.time()
            currTime = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
            with open("ChatLog.txt", mode="a+", encoding="utf-8") as chatLog:
                if message is not "":

                    chatLog.write(currTime + " You: " + message.decode() + "\n")
            clientSocket.send(message)
