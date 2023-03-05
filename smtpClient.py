from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n web server test"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('recv 220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('recv1 250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailFrom = "MAIL FROM:<test@test.com>\r\n"
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != '220':
        #print('recv2 220 reply not received from server.')

    # Send RCPT TO command and handle server response.
    rcptTo = "RCPT TO:<test2@test.com>\r\n"
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '220':
        #print('recv3 220 reply not received from server.')

    # Send DATA command and handle server response.
    data = "DATA\r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '220':
        #print('recv 4 220 reply not received from server.')

    # Send message data.
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    #print(recv5)
    #if recv5[:3] != '220':
        #print('recv 5 220 reply not received from server.')

    # Send QUIT command and handle server response.
    quit = "QUIT\r\n"
    clientSocket.send(quit.encode())
    recv6 = clientSocket.recv(1024).decode()
    #print(recv6)
    #if recv6[:3] != '220':
        #print('recv 6 220 reply not received from server.')

    clientSocket.close()
    #print('Ok')

if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')