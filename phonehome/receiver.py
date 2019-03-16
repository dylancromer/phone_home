import socket

def open_bottle():
    sock = socket.socket()
    port = 1331
    sock.bind(('', port))

    sock.listen(5)
    conn,addr = sock.accept()

    print(f"Got connection from {addr}")
    while True:
        data = conn.recv(1024)
        if data is not None:
            print(data)
            break
    conn.close()
