import socket

target = str(input("Insire an url: "))
ports = [21, 23, 80, 443, 8080]

for port in ports:
    # AF_INET = IP
    # SOCK_STREAM = TCP
    # Criando um cliente no protocolo TCP/IP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)
    code = client.connect_ex((target, port))
    if code == 0:
        print(f"{port} OPEN")


