#! python3

#script for prepeartion of the list of states with their capital cities


import pyperclip
import re
from itertools import izip

stateRegex = re.compile(r'[A-Z]{1}[a-z]+')

text = str(pyperclip.paste())
matches = []
for string in stateRegex.findall(text):
	matches.append(string)
	
print(matches)

	