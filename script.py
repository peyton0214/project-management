import glob 
import pylint.epylint

checks = 'C0301,E1101,W0401,R0201,C0111'

def check_file(filename):
	print('Checking', filename)
	(pylint_stdout, pylint_stderr) = \
		pylint_epylint.py_run(filename + ' --disable=all --enable ' + checks, return_std = True)
	print(pylint_stdout.getvalue())

for filename in glob.glob('*.py'):
	check_file(filename)
