import libmicrocontest,sys,math,time,subprocess,re

def main():
    con = libmicrocontest.commence_contest(16,'kapslock','')
    chaine = con.get_str('chaine')
    print('[+]chaine : '+str(chaine))
    tofind = str(re.search('\d{3}.\d+',str(chaine)).group())
    print('[+]Floating number :: '+str(tofind))
    con.append_answer('nombre',str(tofind))
    print(con.submit_answer())
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()