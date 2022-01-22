import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = socket.gethostname()
print(f'Hostname: {host}')
port = 8081

client.connect((host, port))

# allow maximum data size received from the server
message = client.recv(1024)
print(message.decode('ascii'))

client.close()
