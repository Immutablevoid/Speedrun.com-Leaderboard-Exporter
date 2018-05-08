import os
from scripts import cleanup
from scripts import setupConfig
from scripts import getRuns

# Initiate Startup
try:
	import config as cfg
except (ModuleNotFoundError, NameError) as error:
	from scripts import setupConfig
	setupConfig.setup()
	cleanup.Clean()
	exit()

# User input: Choose which mode to use
def main():

	os.system("title Select option...")
	os.system('cls')
	
	print('''Important Notice:
Ensure ALL instances of this script are closed before starting this script!
If need be, close all windows and restart the script!\n\n''')
	
	print('What would you like to do?\n1. Export Speedrun Leaderboard\n2. Export User Leaderboard\n3. Exit\n')
	option = str(input('Select option (1, 2, 3): '))
	
	if option == '1':
		setupConfig.setup()
		getRuns.SpeedrunLeaderboard(cfg.game, cfg.category, cfg.query)
	elif option == '2':
		setupConfig.setup()
		getRuns.UserSpeedruns(cfg.user)
	elif option == '0':
		os.system('cls')
		# This is pointless and only for fun
		penguin = '''
      .---. 
     /     \ 
    | O _ O | meep
    /  \_/  \   meep
  .' /     \ `. 
 / _|       |_ \ 
(_/ |       | \_) 
    \       / 
   __\_>-<_/__ 
   ~;/     \;~ 
'''
		print(penguin)
		cleanup.Clean()
		exit()
	elif option == '3':
		cleanup.Clean()
		exit()
	else:
		main()