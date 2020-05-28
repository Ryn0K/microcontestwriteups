#!/usr/bin/python
#Written by krn_bhargav(kapslock)
from libmicrocontest2_python27 import * # External library given by website should be in same directory.
import sys,time,os,subprocess,imaplib,email

def main():
    username = ""
    password = ""
    imap_server  = "imap.gmail.com"
    c = commence_contest(21,'kapslock','')
    number = c.get_int('number')
    print("[+]Number : "+str(number))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
