import sys
import socket
import selectors
import types

sel = selectors.DefaultSelector()


def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print("accepted connection from", addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"") #simple object with the attributes of: address, inb and outb
    events = selectors.EVENT_READ | selectors.EVENT_WRITE #want to know when the connection is ready for reading and writing
    sel.register(conn, events, data=data) #data is an opaque object


def service_connection(key, mask):
    sock = key.fileobj #would be the socket
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print("closing connection to", data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("echoing", repr(data.outb), "to", data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]


if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host> <port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((host, port))
lsock.listen()
print("listening on", (host, port))
lsock.setblocking(False) #will not interrupt the main program
sel.register(lsock, selectors.EVENT_READ, data=None) #interested in only data that is ready to be read

try:
    while True:
        events = sel.select(timeout=None) #blocks until the socket is ready for I/O and returns events
        for key, mask in events:
            if key.data is None: #if there is no data, client socket must have been accepted
                accept_wrapper(key.fileobj)
            else:
                # print(key,mask)
                service_connection(key, mask)
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()
