#! python 3

import sys, pyperclip

PASSWORDS = {'email': 'DAW5sfsDAawE2$@#$Ddasa',
			 'blog': 'DAWr#fasasAWDTRGDFADqe2qaw',
			 'luggage': '12345'}
			 
if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy password to given account')
	sys.exit

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password to account ' + account + ' was copied to clipboard.')
else:
		print('The account' + account + 'does not exist.')