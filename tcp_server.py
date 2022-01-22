import socket

# socket object
server = socket.socket(
    family=socket.AF_INET,
    type=socket.SOCK_STREAM
)

host = socket.gethostname()
print(f'Hostname: {host}')
port = 8081

# bind host and port to server
server.bind((host, port))
server.listen(5)

while True:
    # establish connection, accept TCP connection from the client
    client, address = server.accept()
    print(f'Connection received from {address}')

    message = f'Thank you for connecting to the server.\r\n'
    client.send(message.encode('ascii'))
    client.close()
