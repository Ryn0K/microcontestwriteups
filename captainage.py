import libmicrocontest,sys,os,subprocess
c = libmicrocontest.commence_contest(14,'kapslock','')
birth = c.get_int('naissance')
current = c.get_int('date_courante')
age = current - birth
c.append_answer('age',age)
print(c.submit_answer())