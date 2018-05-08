import os
import shutil
	
def Clean():
	# Delete __pycache__
	path = os.getcwd()
	
	while True:
		try:
			shutil.rmtree('%s/__pycache__' % path, ignore_errors=False, onerror=None)
			shutil.rmtree('%s/scripts/__pycache__' % path, ignore_errors=False, onerror=None)
		except FileNotFoundError:
			break