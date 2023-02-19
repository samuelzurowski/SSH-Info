import paramiko
import socket
import sys

def seperate(name):
    print("*"* 15 + ' ' +  name + ' ' + "*" * 15)

def footer():
    print("*"* 30)

PORT = 22
HOST = ""

if len(sys.argv) < 2:
    print(f"{sys.argv[0]} <ip> [port]")
    sys.exit()

if len(sys.argv) > 2:
    PORT = int(sys.argv[2])

HOST = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    opts = paramiko.transport.Transport(s).get_security_options()

    ciphers = opts.ciphers

    kex = opts.kex

    digests = opts.digests

    key_types = opts.key_types

    seperate("CIPHERS")
    for cipher in ciphers:
        print(cipher)

    seperate("KEX")
    for ex in kex:
        print(ex)

    seperate("DIGESTS")
    for d in digests:
        print(d)

    seperate("KEY_TYPES")
    for k in key_types:
        print(k)
