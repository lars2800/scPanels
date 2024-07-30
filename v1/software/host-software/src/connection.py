import socket


def runServer(serverAddr:tuple[str,int],onMsgCallback):

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server.bind(serverAddr)
    server.listen()
    
    client = server.accept()[0]
    client.setblocking(False)

    while ( True ):

        try:
            r = client.recv(4096*4)
            
            if (r.decode() != ""):

                onMsgCallback(r.decode())

        except BlockingIOError:
            pass