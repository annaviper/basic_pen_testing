import socket


def banner(ip, port):
    sock = socket.socket()
    try:
        sock.connect((ip, int(port)))
        sock.settimeout(5)
        print(str(sock.recv(1024)))
    except Exception as e:
        print(str(e))


def main():
    ip = input("Enter IP: ")
    port = int(input("Enter port: "))
    banner(ip, port)


if __name__ == "__main__":
    main()
