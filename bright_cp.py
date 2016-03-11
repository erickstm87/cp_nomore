#!/usr/bin/env python
import webbrowser
import sys
import os
import pyautogui
from subprocess import call
import re


file1 = open('basics_stage3.txt', 'r')
#new = 1
new_file = []
b_rowser = input('do you want to run this in safari, chrome, or firefox? Make sure to type your choice exactly as it appears \n')
#b_rowser = 'firefox'
if b_rowser == 'safari':
    b = webbrowser.get('safari')
    bashCommand = "sudo killall 'Safari' "
elif b_rowser == 'chrome':
    b = webbrowser.get()
    bashCommand = "sudo killall 'google' "
elif b_rowser == 'firefox':
    b = webbrowser.get('firefox')
    #for row in file1:
	#	new_file.append(row)


for i in file1:
	'''urls = i.split(',')
	for url in urls:
		url_trimmed = url.strip()
		new = 1'''
	b.open(i,new=1)
	print(i)
	control = input('hit enter for next test case, skip to skip the test case, or fail to indicate the test case as failed \n')
	if control == 'fail':
		x = input('why did it fail? \n')
		#else:
		with open('results2.txt', 'a') as f:
    			f.write('fail(%s),'% x + i) 
	elif control == 'skip':
		with open('results2.txt','a') as f:
				f.write('skipped,'+i)
	else:
		with open('results2.txt', 'a') as f:
    			f.write('pass,' + i)
		continue
	#elif control == 'fail':
	#pdb.set_trace()