import sys
from os import listdir

def toPythonString(str):
	str = str.replace('_', ' ').replace('{COL}', ':').replace('{LT}', '<').replace('{GT}', '>')
	return str[1:] + '\n'

code = map(toPythonString, sorted(listdir('code')))

with open('out.py', 'w') as outFile:
	outFile.writelines(code)

import out
print out.qsort([3, 2, 1])
