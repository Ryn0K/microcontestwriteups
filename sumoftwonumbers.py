#!/usr/bin/python
#Written by krn_bhargav(kapslock)
from libmicrocontest2_python27 import * # External library given by website should be in same directory.
import sys,os,subprocess

c = commence_contest(1,'kapslock','')
a = c.get_int('a')
b = c.get_int('b')
s = a+b
c.append_answer('s',s)
print(c.submit_answer())
