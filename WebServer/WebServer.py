# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
port = 6789
serverSocket.bind(('', port))
print("Server socket binded to port {}".format(port))
serverSocket.listen(1)
print("Server socket is listening")
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')
    # Fill in start
    connectionSocket, addr = serverSocket.accept()
    print('Connected by', addr)
    # Fill in end

    try:
        # Fill in start
        message = connectionSocket.recv(1024)
        if not message:
            connectionSocket.close()
            continue
        # Fill in end

        filename = message.split()[1]
        print('File name: ', filename)
        f = open(filename[1:])

        # Fill in start
        outputdata = f.read()
        print(outputdata)
        # Fill in end

        # Send one HTTP header line into socket
        # Fill in start
        header_line = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(header_line.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.close()

    except IOError:
        # Send response message for file not found
        # Fill in start
        response_header = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(response_header.encode())
        response_message = '<!DOCTYPE html><html><head><title> 404 Not Found </title></head><body><h1> 404 Not Found </h1></body></html>\r\n'
        connectionSocket.send(response_message.encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
