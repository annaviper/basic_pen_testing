import socket


def create_socket():
    sock = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )
    sock.settimeout(5)
    return sock


def scan_port(sock, host, port):
    # connect_exc return error code instead of exception which is easy to handle
    if sock.connect_ex((host, port)):
        print("Port is down.")
    else:
        print("Port is up.")


def main():
    sock = create_socket()
    host = input("Enter your IP: ")
    port = int(input("Enter the port: "))
    scan_port(sock, host, port)


if __name__ == "__main__":
    main()
