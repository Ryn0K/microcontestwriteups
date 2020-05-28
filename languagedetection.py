import libmicrocontest,sys,os,subprocess
from langid import classify

def main():
    con = libmicrocontest.commence_contest(37,'kapslock','kkbhargavmail58525852Kb@')
    txt1 = con.get_str('txt1')
    txt2 = con.get_str('txt2')
    txt3 = con.get_str('txt3')
    txt4 = con.get_str('txt4')
    print('[+]txt1 : '+txt1)
    print('[+]txt2 : '+txt2)
    print('[+]txt3 : '+txt3)
    print('[+]txt4 : '+txt4)
    lang1 = classify(txt1)
    lang2 = classify(txt2)
    lang3 = classify(txt3)
    lang4 = classify(txt4)
    l1 = lang1[0]
    l2 = lang2[0]
    l3 = lang3[0]
    l4 = lang4[0]
    if l1 == 'nl':
        l1 = 'du'
    if l2 == 'nl':
        l2 = 'du'
    if l3 == 'nl':
        l3 = 'du'
    if l4 == 'nl':
        l4 = 'du'    
    con.append_answer('lang1',l1)
    con.append_answer('lang2',l2)
    con.append_answer('lang3',l3)
    con.append_answer('lang4',l4)
    print(con.submit_answer())
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()