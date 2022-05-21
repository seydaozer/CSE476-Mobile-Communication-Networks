from socket import *
from time import *

# server address
server_addr = ('localhost', 12000)
# client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
# set the timeout value on the clientSocket
clientSocket.settimeout(1)

min_rtt = 0
max_rtt = 0
sum_rtt = 0
response_count = 0

for i in range(1, 11):
    try:
        sendTime = time()
        client_message = 'Ping ' + str(i) + ' ' + str(strftime("%H:%M:%S"))
        # send the ping message using UDP
        clientSocket.sendto(client_message.encode(), server_addr)
        print('Client send the message: ' + client_message)

        # Is there a response message from the server?
        response_message, server_address = clientSocket.recvfrom(1024)
        # if any, print the response message from server
        print("Response message from server: " + response_message.decode())
        responseTime = time()
        response_count = response_count + 1

        # calculate and print RTT, if server responses
        rtt = responseTime - sendTime
        print('Round Trip Time (RTT): ' + str(rtt) + ' seconds')

        sum_rtt += rtt

        if i == 1:
            min_rtt = rtt
            max_rtt = rtt

        if rtt < min_rtt:
            min_rtt = rtt

        if rtt > max_rtt:
            max_rtt = rtt

    # otherwise, print "Request timed out"
    except timeout:
        print('Request timed out')

clientSocket.close()

print('------------------------------')
print('minimum RTT: ' + str(min_rtt) + ' seconds')
print('maximum RTT: ' + str(max_rtt) + ' seconds')

avg_rtt = sum_rtt / response_count
print('average RTT: ' + str(avg_rtt) + ' seconds')

packet_loss_rate = (10 - response_count) * 10
print('packet loss rate: %' + str(packet_loss_rate) + '')
print('------------------------------')

