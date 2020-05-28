#!/usr/bin/python
#Written by krn_bhargav(kapslock)
from libmicrocontest2_python27 import * # External library given by website should be in same directory.
import sys,os,subprocess,pytesseract
from PIL import Image

def main():
    con = commence_contest(20,'kapslock','')
    img = con.get_str('img')
    with open('img.png','w') as f:
        f.write(img)
        f.close()
    value = Image.open('img.png')
    text = pytesseract.image_to_string(value,lang='eng')
    print('[+]text :: '+text)
    con.append_answer('text',text)
    print(con.submit_answer())
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
