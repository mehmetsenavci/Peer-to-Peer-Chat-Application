import socket, time, datetime

usersAsList = list()
usersAsDict = dict()

with open("Users.txt", "r+", encoding="utf-8") as users:
    lines = users.readlines()
    for line in lines:
        line = line.strip("\n")
        usersAsList.append(line.split(","))

for name, ip in usersAsList:
    usersAsDict[ip] = name

while True:

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(("", 5001))
    serverSocket.listen(1)
    print("Server is ready to recive.")

    #while True:
    connectionSocket, address = serverSocket.accept()

    while True:
        #print(address)
        # print("Please type quit to terminate the program")
        
        # Gets the current time with the formal form.
        timestamp = time.time()
        currTime = datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

        message = connectionSocket.recv(1024)
        if message.decode() == "quit":
            serverSocket.close()
            break
        
        print(currTime + " " + usersAsDict[address[0]] + ": " + message.decode('utf-8'))
        
    
        with open("ChatLog.txt", mode="a+", encoding="utf-8") as chatLog:
            if message is not "":
                chatLog.write(currTime + " " + usersAsDict[address[0]] + ": " + message.decode() + "\n")

    


        
        
        
