from libmicrocontest import *
import subprocess
from bs4 import BeautifulSoup
import re
def main():
    subprocess.call(['clear'])
    c = commence_contest(44,'kapslock','') #password in left blank
    username = c.get_str('username')
    url = "http://www.wechall.net/en/profile/"+str(username)
    subprocess.call(['curl',url,'-o','url.txt'])
    with open('url.txt','r') as f:
        web = BeautifulSoup(f,'lxml')
        d = web.find('div',{'class','fl'})
        scrap=d.find('table').text
        un = str(re.search('Username(.*)',str(scrap)).group(1)).strip()
        if (un == username):
            score = str(re.search('Score(.*)',str(scrap)).group(1)).strip()
            print('Score :: '+score)
            rank = str(re.search('Global Rank(.*)',str(scrap)).group(1)).strip()
            print('Rank :: '+rank)
            Rdate = str(re.search('Register Date(.*)',str(scrap)).group(1)).strip()
            print('Register_date :: '+Rdate)
            Lactivity = str(re.search('Last Activity(.*)',str(scrap)).group(1)).strip()
            print('Last Activity :: '+Lactivity)
            c.append_answer('score',score)
            c.append_answer('rank',rank)
            c.append_answer('register_date',Rdate)
            c.append_answer('last_activity',Lactivity)
            print(c.submit_answer())
        else:
            print("Something wrong")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()