#!/usr/bin/python
#Written by krn_bhargav(kapslock)
from libmicrocontest2_python27 import * # External library given by website should be in same directory.
import sys,math,time,subprocess

def main():
    con = commence_contest(3,'kapslock','')  #your password for contest
    text = str(con.get_param('texte',str)).strip()
    mot = str(con.get_param('mot',str)).strip()
    print('[+]text :: '+text)
    print('[+]mot :: '+mot)
    #using count method to find the occurence of variable string mot in text
    occ = text.count(mot)
    print('[+]occ :: '+str(occ))
    con.append_answer('occ',occ)
    print(con.submit_answer())
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
