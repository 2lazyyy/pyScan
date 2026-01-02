import sys
import os
import socket

def scan_portTCP(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{ip}:{port} OPEN")
        sock.close()
    except socket.error:
        pass
    finally:
        sock.close()


def main():
    
    if len(sys.argv) != 2:
        print("Usage: python script.py <file | ip | domain>")
        sys.exit(1)
    
    host = sys.argv[1]
    start_port = 1
    end_port = 1000

    if os.path.isfile(host):
        with open(host, 'r') as f:
            for line in f:
                target = line.strip()
                if not target:
                    continue

                print(f"Scanning ports on {target} ...")
                for port in range(start_port, end_port + 1):
                    scan_portTCP(target, port)


    else:
        print(f"Scanning ports on {host} ...")
        for port in range(start_port, end_port + 1):
            scan_portTCP(host, port)



if __name__ == "__main__":
    main()



