import libmicrocontest,sys,time,os,subprocess,imaplib,email

def main():
    username = "kkbhargavmail@gmail.com"
    password = "110727272"
    imap_server  = "imap.gmail.com"
    c = libmicrocontest.commence_contest(21,'kapslock','')
    number = c.get_int('number')
    print("[+]Number : "+str(number))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()