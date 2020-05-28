import libmicrocontest,os,sys,time

def main():
    con = libmicrocontest.commence_contest(43,'kapslock','')
    s1 = con.get_str('s')
    print('[+]s1 :: '+str(s1))
    s1_rev = s1[::-1] # reverse slicing method
    print('[+]string reversed :: '+str(s1_rev))
    con.append_answer('s_rev',s1_rev)
    print(con.submit_answer())
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()