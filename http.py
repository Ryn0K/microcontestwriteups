#!/usr/bin/python
#Written by krn_bhargav(kapslock)
from libmicrocontest2_python27 import * # External library given by website should be in same directory.
import subprocess,bs4
def main():
    c = commence_contest(15,'kapslock','') # password in left blank
    x = c.get_int('x')
    print("[Get] "+str(x))
    url = "http://www.microcontest.com/contests/15/nombre.php"
    r = subprocess.check_call(['curl',url+'?x='+str(x),'-o','url.txt'])
    with open('url.txt','r') as f:
        web = bs4.BeautifulSoup(f,'lxml')
        d = web.p.text
        print('[Found] '+str(d))
        c.append_answer('y',d)
        print(c.submit_answer())
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
