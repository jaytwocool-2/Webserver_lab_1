# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
serverPort = 6789                         # choose a non-privileged port (e.g., 6789)
serverSocket.bind(('', serverPort))       # bind to all interfaces on serverPort
serverSocket.listen(1)                    # allow one queued connection (handles one at a time)
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start  # Fill in end
    try:
        message = connectionSocket.recv(1024).decode()  # Fill in start  # Fill in end

        # If the client closes immediately or sends nothing, just close and continue
        if not message:
            connectionSocket.close()
            continue

        filename = message.split()[1]  # e.g., "/HelloWorld.html"
        f = open(filename[1:], 'r', encoding='utf-8')  # strip leading "/"
        outputdata = f.read()  # Fill in start  # Fill in end
        f.close()

        # Send one HTTP header line into socket
        # Fill in start
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
        connectionSocket.send(header.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        body = "<html><head><title>404 Not Found</title></head><body><h1>404 Not Found</h1></body></html>"
        header = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
        connectionSocket.send(header.encode())
        connectionSocket.send(body.encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  
