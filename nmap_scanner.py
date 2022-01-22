import nmap


def choose_scan_type():
    ip = input('Please enter the IP address to scan:\n')
    resp = input("""
        Enter scan type to run:
        1 - SYN ACK
        2 - UDP
        3 - COMPREHENSIVE
        """)
    print(f"Scanning {ip}...")
    return ip, resp


def scan(scanner, ip, s_methods, s_type):
    print(f"Nmap Version\t {scanner.nmap_version()}")
    print(f"Scan info:\t {scanner.scan(ip, '1-1024', s_methods)}")
    print(scanner.scaninfo())

    print(f"IP Status:\t {scanner[ip].state()}")
    print(f"Protocols:\t {scanner[ip].all_protocols()}")
    print(f"Open Ports:\t {scanner[ip][s_type].keys()}")


def scan_choice(resp, scanner, ip):
    mapping = {
        '1': scan(scanner, ip, '-v sS', 'tcp'),
        '2': scan(scanner, ip, '-v sU', 'udp'),
        '3': scan(scanner, ip, '-v -sS -sV -sC -A -O', 'tcp')
    }

    if resp in mapping.keys():
        mapping[resp]()
    else:
        print('Wrong selection.')


def main():
    scanner = nmap.PortScanner()
    print("Welcome to nmap tool")

    ip, scan_type = choose_scan_type()
    scan_choice(scan_type, scanner, ip)


if __name__ == '__main__':
    main()
