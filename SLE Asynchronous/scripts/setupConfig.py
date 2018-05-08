import os

def setup():
	os.system('cls') 
	# Check if config.py exists
	if os.path.isfile('config.py'):
		pass
	else:
		print('config.py not found... Creating new file...')
		configDir = open("config.py", 'w', encoding='utf-8')
		msg = 	"""# Set game information\n
# use either username or speedrun.com user ID:
# user = \'y8dwlrgj\' or \'timetravelpenguin\'
user = \'timetravelpenguin\'
game = \'smo\'
category = \'any\'

# Query should be in form: \'?conditionA=1&condintionB=2&conditionC=3\'
# For more query filter options, visit:
# https://github.com/speedruncomorg/api/blob/master/version1/runs.md#get-runs\

# For no filter, query = \'\'
query = \'?emulators=false\'
"""
		configDir.write(msg)
		configDir.close()
		print('Please edit config.py, and then rerun SLE.py...\n')
		os.system('pause')