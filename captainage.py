#!/usr/bin/python
#Written by krn_bhargav(kapslock)
from libmicrocontest2_python27 import * # External library given by website should be in same directory.
import sys,os,subprocess
c = commence_contest(14,'kapslock','')
birth = c.get_int('naissance')
current = c.get_int('date_courante')
age = current - birth
c.append_answer('age',age)
print(c.submit_answer())
