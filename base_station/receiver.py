from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('192.168.8.125', 8000))
while True:
    print('listening on port 8000...')
    data, addr = s.recvfrom(1024)
    print('\nReceived:\t{}\nFrom:\t\t{}\n\n'.format(data, addr[0]))
    if data == 'moshimoshi?':
        s.sendto('damn bro you watch anime?', addr)
    else:
        s.sendto('sup playa what\'s kickin\'', addr)
