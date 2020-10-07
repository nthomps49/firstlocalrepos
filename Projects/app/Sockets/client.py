import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.29"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Hello World!")
send("Hello Everyone!")
send("Hello Me!")
send(DISCONNECT_MESSAGE)






















#import socket
#
#HEADERSIZE = 10
#
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((socket.gethostname(), 1234))
#
#while True:
#
#   full_msg = ''
#    new_msg = True
#    while True:
#        msg = s.recv(16)
#        if new_msg:
#            print(f"new message length: {msg[:HEADERSIZE]}")
#            msglen = int(msg[:HEADERSIZE])
#            new_msg = False
#            
#        full_msg += msg.decode("utf-8")
#
#        if len(full_msg)-HEADERSIZE == msglen:
#            print("full msg recvd")
#            print(full_msg[HEADERSIZE:])
#            new_msg = True
#            new_msg = ''
##
# #   print(msg.decode("utf-8"))







