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

def Quit():
	cleanup.Clean()
	exit()

# User input: Choose which mode to use
def main():

	os.system("title Select option...")
	os.system('cls')
	
	print('What would you like to do?\n1. Export Speedrun Leaderboard\n2. Export User Leaderboard\n3. Search Variables\n4. Exit\n')
	option = str(input('Select option (1, 2, 3, 4): '))
	
	if option == '1':
		getRuns.SpeedrunLeaderboard(cfg.game, cfg.category, cfg.query)
	elif option == '2':
		getRuns.UserSpeedruns(cfg.user)
	elif option == '3':
		RAWcategories, PARSEcategories, max_categories, fullGameName = getRuns.getCategories(cfg.game)
		getRuns.FindVariables(cfg.game, RAWcategories, PARSEcategories, max_categories, fullGameName)
	elif option == '4':
		Quit()
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
		Quit()
	else:
		main()