import libmicrocontest,sys,os,subprocess

c = libmicrocontest.commence_contest(1,'kapslock','')
a = c.get_int('a')
b = c.get_int('b')
s = a+b
c.append_answer('s',s)
print(c.submit_answer())