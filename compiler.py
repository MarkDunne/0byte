import sys
from os import listdir

def toPythonString(str):
	str = str.replace('_', ' ').replace('{COL}', ':').replace('{LT}', '<').replace('{GT}', '>')
	return str[1:] + '\n'

code = map(toPythonString, sorted(listdir('code')))

outFile = open('out.py', 'w')
outFile.writelines(code)
outFile.close()

import out
print out.qsort([1,2,3])