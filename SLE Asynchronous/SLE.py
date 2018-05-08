import os
from scripts import main
from scripts import cleanup

def Quit():
	cleanup.Clean()
	exit()

# The commented code is currently not needed!!!	
	
def LibraryCheck():
	os.system('cls')
	try:
		# import srcomapi
		import gevent
	except ModuleNotFoundError:
		print('You are missing the srcomapi library...\nPlease run the libraryInstall.bat file as Administrator to install them!\n')
		Quit()

LibraryCheck()
main.main()
Quit()