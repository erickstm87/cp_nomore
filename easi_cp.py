#!/usr/bin/env python
import webbrowser
import sys
import os
from subprocess import call
import re
import csv

b_rowser = raw_input('do you want to run this in safari, chrome, or firefox? Make sure to type your choice exactly as it appears \n')
#b_rowser = 'firefox'
if b_rowser == 'safari':
    b = webbrowser.get('safari')
    bashCommand = "sudo killall 'Safari' "
elif b_rowser == 'chrome':
    b = webbrowser.get()
    bashCommand = "sudo killall 'google' "
elif b_rowser == 'firefox':
    b = webbrowser.get('firefox')
   
with open('easi.csv','w') as fh:
	reader = csv.reader(fh)
	for row in reader:
		for c,j in enumerate(row):
	    		if 'https' in j:
	    			print(row)
	    			b.open(j,new=0)
	    			control = raw_input('hit enter for next test case, skip to skip the test case, or fail to indicate the test case as failed \n')
					if control == 'fail':
						x = raw_input('why did it fail? \n')
						#else:
						with open('results.txt', 'a') as f:
				    			f.write('fail(%s),'% x + r) 
					elif control == 'skip':
						with open('results.txt','a') as f:
								f.write('skipped,'+r)
					else:
						with open('results.txt', 'a') as f:
				    			f.write('pass,' + r)
						continue
		