from socket import *
from base64 import *
import ssl

msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'

# Choose a mail server (e.g. Google mail server) and call it mailserver
# Fill in start
mailserver = ('smtp.gmail.com', 587)
# Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
# 1 - Opening the connection
clientSocket.connect(mailserver)
print('connected to gmail server\n')
# Fill in end

recv = clientSocket.recv(1024)
print(recv.decode())
if recv[:3].decode() != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
print('HELO command')
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1.decode())
if recv1[:3].decode() != '250':
    print('250 reply not received from server.')

# 2 - Using a secure connection (tls)
# START TLS command
print('START TLS command')
TLSCommand = "STARTTLS\r\n"
clientSocket.send(TLSCommand.encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())
if recv2[:3].decode() != '220':
    print('220 reply not received from server.')
# ssl - TLS/SSL wrapper for socket objects
tlsSocket = ssl.wrap_socket(clientSocket)

# 3 - Creating the email
gmail_user = "mynetworkproject0@gmail.com"
gmail_password = "networkproject"

# 4 - Authenticating with Gmail
# 2-step verification
print('AUTH user email')
tlsSocket.send('AUTH LOGIN '.encode() + b64encode(gmail_user.encode()) + '\r\n'.encode())
recv3 = tlsSocket.recv(1024)
print(recv3.decode())
if recv3[:3].decode() != '334':
    print('334 reply not received from server.')
print('AUTH user password')
tlsSocket.send(b64encode(gmail_password.encode()) + "\r\n".encode())
recv4 = tlsSocket.recv(1024)
print(recv4.decode())
if recv4[:3].decode() != '235':
    print('235 reply not received from server.')

# 5 - Sending the Email
# Send MAIL FROM command and print server response.
# Fill in start
print('MAIL FROM command')
mailFrom = "MAIL FROM: <mynetworkproject0@gmail.com>\r\n"
tlsSocket.send(mailFrom.encode())
recv_mail = tlsSocket.recv(1024)
print(recv_mail.decode())
if recv_mail[:3].decode() != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
print('RCPT TO command')
rcptToCommand = "RCPT TO: <seydaozer17@gmail.com>\r\n"
tlsSocket.send(rcptToCommand.encode())
recv_rcpt = tlsSocket.recv(1024)
print(recv_rcpt.decode())
if recv_rcpt[:3].decode() != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
print('DATA command')
dataCommand = "DATA\r\n"
tlsSocket.send(dataCommand.encode())
recv_data = tlsSocket.recv(1024)
print(recv_data.decode())
if recv_data[:3].decode() != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
print('Send message data')
message = "Subject: simple mail client \r\n\r\n" + msg + endmsg
tlsSocket.send(message.encode())
recv_msg = tlsSocket.recv(1024)
print(recv_msg.decode())
if recv_msg[:3].decode() != '250':
    print('250 reply not received from server.')
# Fill in end
# Message ends with a single period.
# Fill in start

# Fill in end

# Send QUIT command and get server response.
# Fill in start
print('QUIT command')
tlsSocket.send("QUIT\r\n".encode())
recv_quit = tlsSocket.recv(1024)
print(recv_quit.decode())
if recv_quit[:3].decode() != '221':
    print('221 reply not received from server.')
# Fill in end

tlsSocket.close()

