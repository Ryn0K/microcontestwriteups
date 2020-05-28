#!/usr/bin/python
#Written by krn_bhargav(kapslock)
from libmicrocontest2_python27 import * # External library given by website should be in same directory.
import sys,math,time,subprocess,re

def main():
    con = commence_contest(16,'kapslock','')
    chaine = con.get_str('chaine')
    print('[+]chaine : '+str(chaine))
    tofind = str(re.search('\d{3}.\d+',str(chaine)).group())#extract floating point number
    print('[+]Floating number :: '+str(tofind))
    con.append_answer('nombre',str(tofind))
    print(con.submit_answer())
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
