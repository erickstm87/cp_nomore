#!/usr/bin/env python
import webbrowser
import csv
import sys
import os
import time
from subprocess import call
import random
import pdb 
import pyautogui

file1 = open('easi_urls.txt', 'r')
new = 1
b_rowser = input('do you want to run this in safari, chrome, or firefox? Make sure to type your choice exactly as it appears \n')
if b_rowser == 'safari':
    b = webbrowser.get('safari')
elif b_rowser == 'chrome':
    b = webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
elif b_rowser == 'firefox':
    b = webbrowser.get('firefox')
#b = webbrowser.get('safari')
for i in file1:
	new = 1
	b.open(i,new=0)
	control = input('hit n for next test case or fail to indicate the test case as failed \n')
	if control == 'n':
		with open('results2.txt', 'a') as f:
    			f.write('pass,' + i)
		continue
	#elif control == 'fail':
	else:
		with open('results2.txt', 'a') as f:
    			f.write('fail,'+i)
	#pdb.set_trace()