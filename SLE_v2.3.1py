## Made by TimeTravelPenguin
## Check for updates at https://SLE.pengu.space
## Or simply visit https://pengu.space for more general stuff

import urllib.request
import json
import os
import datetime
import time
import math
import shutil

# Set title and clock
os.system("title Waiting for user input...")
os.system('chcp 65001')

start = time.time()
time.clock()
elapsed = 0

def setupConfig():
	os.system('cls') 
	# Check if config.py exists
	if os.path.isfile('config.py') == True:
		pass
	else:
		os.path.isfile('config.py')
		print('config.py not found... Creating new file...')
		configDir = open("config.py", 'w', encoding='utf-8')
		msg = "# Set game information\n# username / ID\n# user = \'y8dwlrgj\'\nuser = \'timetravelpenguin\'\ngame = \'smo\'\ncategory = \'any\'\n\n# if displaySec = True, the on screen time will be in seconds rather than HH:MM:SS\n# if exportSec = True, the exported time will be in seconds rather than HH:MM:SS\n# user_ is for the userboards, leaderboard_ is for the speedrunning leaderboard\nleaderboard_displaySec = False\nleaderboard_exportSec = True\nuser_displaySec = False\nuser_exportSec = True\n\n# Query should be \'?conditionA=1&condintionB=2&conditionC=3\'\n# For more query filter options, visit:\n# https://github.com/speedruncomorg/api/blob/master/version1/runs.md#get-runs\n\n# For no filter, query = \'\'\nquery = \'?emulators=false\'\n\n# Statistics Mode\n# Set to True if you wish to ignore usernames, and only export the time for speedrun leaderboards\n# This will significantly increase the speed of the export\nstatMode = True\n"
		configDir.write(msg)
		configDir.close()
		print('Please edit config.py, and then rerun SLE.py...\n')
		Cleanup()
	
	# Code config.py Boolean check here

def startText():
	# Start up text
	os.system('cls')
	print("This python script was written and coded by TimeTravelPenguin")
	print()
	print("For more, goto: https://SLE.pengu.space")
	print()
	os.system("title Connecting to API...")
	
def LeaderboardExport():
	
	os.system('cls')
	
	mode = input('Would you like to use Statistics mode?\nOption (0=yes, 1=no): ')
	if mode == "0":
		statMode = True
	elif mode == "1":
		statMode = False
	else:
		LeaderboardExport()

	startText()

	gamename = IDtoGame(game)
	
	print("==========================================================================")
	print()
	time_var = datetime.datetime.now()
	print(time_var)
	print('\nGame: %s (%s)' % (gamename, game))
	print('Category: ' + category)
	if query == '':
		print('Query: None')
	else:
		print('Query: ' + query)
	print('Statistics Mode = %s\n' % str(statMode))

	# Load leaderboard API
	api_url = 'https://www.speedrun.com/api/v1/leaderboards/%s/category/%s%s' % (game, category, query)
	response = urllib.request.urlopen(api_url).read()
	json_obj = str(response, 'utf-8')
	api_data = json.loads(json_obj)

	file = open("SLE_Export_%s_%s.txt" % (game, category), 'w', encoding='utf-8')

	file.write('%s\n\n' % time_var)
	
	# Title information for time and percentage	
	max_runs = len(api_data['data']['runs'])
	count = 0
	errors = 0

	# List leaderboard data
	for item in api_data['data']['runs']:
		place = item['place']
		runtime = item['run']['times']['primary_t']
		
		# Determine if times are in seconds or H:M:S	
		if leaderboard_displaySec == False:
			display_runtime = secToTime(runtime)
		else:
			display_runtime = runtime
		if leaderboard_exportSec == False:
			export_runtime = secToTime(runtime)
		else:
			export_runtime = runtime
		
		# Check Statistics Mode
		if statMode == False and isinstance(statMode, bool) == True:
			try:
				name_id = item['run']['players'][0]['id']
				user_name = IDtoName(name_id)
				print(place, user_name, secToTime(runtime))
				file.write("%s\t%s\t%s\n" % (place, user_name, runtime))
			except KeyError:
				name_id = item['run']['players'][0]['name']
				print(place, name_id, secToTime(runtime))
				file.write("%s\t%s\t%s\n" % (place, name_id, export_runtime))
			except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as error:
				print("Error...")
				errors += 1
				continue
		elif statMode == True and isinstance(statMode, bool) == True:
			print(place, secToTime(runtime))
			file.write("%s\t%s\n" % (place, runtime))
		else:
			print('\nstatMode should be True or False')
			Cleanup()

		count += 1
		percent = str(round(count * 100 / max_runs, 3))
		fract = "%s/%s" % (count, max_runs) 
		
		elapsed = secToTime(time.time() - start)
		etaTime = secToTime((time.time() - start) * (max_runs / count - 1))

		os.system("title Progress: " + percent + "% (" + fract + ")   Time: " + str(elapsed) + "   Errors: " + str(errors) + "   ETA: " + etaTime)
	file.write("\nCompleted Successfully with %s errors...\n" % errors)
	file.close()
	print("\nCompleted Successfully with %s errors...\n" % str(errors))
	Cleanup()

def UserboardExport():

	startText()

	username = IDtoName(user)

	print("==========================================================================")
	print()
	time_var = datetime.datetime.now()
	print(time_var)
	print('\nUser: %s\n' % username)
	

	# Load leaderboard API
	api_url = 'https://www.speedrun.com/api/v1/users/%s/personal-bests' % user
	response = urllib.request.urlopen(api_url).read()
	json_obj = str(response, 'utf-8')
	api_data = json.loads(json_obj)

	file = open("SLE_Export_%s.txt" % username, 'w', encoding='utf-8')

	file.write('%s\n\n' % time_var)
	
	# Title information for time and percentage	
	max_runs = len(api_data['data'])
	count = 0
	errors = 0

	# List leaderboard data
	for item in api_data['data']:
		while True:
				try:
					place = item['place']
					game_id = item['run']['game']
					game = IDtoGame(game_id)
					category_id = item['run']['category']
					category = IDtoCategory(category_id)
					runtime = item['run']['times']['primary_t']
					platform_id = item['run']['system']['platform']
					platform = IDtoPlatform(platform_id)
					region_id = item['run']['system']['region']
					region = IDtoRegion(region_id)
					emulated = item['run']['system']['emulated']
					
					if user_displaySec == False:
						display_runtime = secToTime(runtime)
					else:
						display_runtime = runtime
						
					print("Place: %s\nGame: %s\nCategory: %s\nRuntime: %s\nPlatform: %s\nRegion: %s\nEmulated: %s\n\n" % (place, game, category, display_runtime, platform, region, emulated))
					
					if user_exportSec == False:
						export_runtime = secToTime(runtime)
					else:
						export_runtime = runtime
						
					file.write("Place: %s\nGame: %s\nCategory: %s\nRuntime: %s\nPlatform: %s\nRegion: %s\nEmulated: %s\n\n" % (place, game, category, export_runtime, platform, region, emulated))
				except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as error:
					print("Error...")
					errors += 1
					continue
				break
		count += 1
		percent = str(round(count * 100 / max_runs, 3))
		fract = "%s/%s" % (count, max_runs)
		
		elapsed = secToTime(time.time() - start)
		etaTime = secToTime((time.time() - start) * (max_runs / count - 1))

		os.system("title Progress: " + percent + "% (" + fract + ")   Time: " + str(elapsed) + "   Errors: " + str(errors) + "   ETA: " + etaTime)
	file.write("\nCompleted Successfully with %s errors...\n" % errors)
	file.close()
	print("Completed Successfully with %s errors...\n" % str(errors))
	Cleanup()

def IDtoGame(game_id):
	# Read game name
	try:
		game_url = 'https://www.speedrun.com/api/v1/games/%s' % game_id
		response_game = urllib.request.urlopen(game_url).read()
		game_obj = str(response_game, 'utf-8')
		game_data = json.loads(game_obj)

		gamename = game_data['data']['names']['international']
		return gamename
	except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as error:
		print("Game ID Error...")
		print("Please check your Internet connection, and that config.py has correct information")
		print()
		os.system('pause')
		return "Error..."

def IDtoCategory(category_id):
	# Read game name
	try:
		category_url = 'https://www.speedrun.com/api/v1/categories/%s' % category_id
		response_category = urllib.request.urlopen(category_url).read()
		category_obj = str(response_category, 'utf-8')
		category_data = json.loads(category_obj)

		gamename = category_data['data']['name']
		return gamename
	except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as error:
		print("Game ID Error...")
		print("Please check your Internet connection, and that config.py has correct information")
		print()
		os.system('pause')
		return "Error..."
		
def IDtoName(name_id):
	try:
		# ID to name conversion
		api_user = 'https://www.speedrun.com/api/v1/users/%s' % (name_id)

		response_user = urllib.request.urlopen(api_user).read()
		json_obj = str(response_user, 'utf-8')

		api_data_user = json.loads(json_obj)
		
		user_name = api_data_user['data']['names']['international']
		return user_name
	except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as error:
		print("Name ID Error...")
		print("Please check your Internet connection...\n")
		os.system('pause')
		return "Error..."

def IDtoPlatform(platform_id):
	try:
		# ID to platform name conversion
		api_user = 'https://www.speedrun.com/api/v1/platforms/%s' % (platform_id)

		response_platform = urllib.request.urlopen(api_user).read()
		json_obj = str(response_platform, 'utf-8')

		api_data_platform = json.loads(json_obj)
		
		platform_name = api_data_platform['data']['name']
		return platform_name
	except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as error:
		print("Platform ID Error...")
		print("Please check your Internet connection...")
		print()
		os.system('pause')
		return "Error..."
	
def IDtoRegion(region_id):
	if region_id == None:
		region_name = "None"
	else:
		try:
			# ID to region name conversion
			api_region = 'https://www.speedrun.com/api/v1/regions/%s' % (region_id)

			response_region = urllib.request.urlopen(api_region).read()
			json_obj = str(response_region, 'utf-8')

			api_data_region = json.loads(json_obj)
			
			region_name = api_data_region['data']['name']
			return region_name
		except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as error:
			print("Region ID Error...")
			print("Please check your Internet connection...")
			print()
			os.system('pause')
			return "Error..."

def secToTime(sec):
	if sec >= 3600:
		m, s = divmod(sec, 60)
		h, m = divmod(m, 60)
		return "%d:%02d:%s" % (h, m, round(s, 3))
	else:
		m, s = divmod(sec, 60)
		return "%d:%s" % (m, round(s, 3))
	

def Cleanup():
	# Delete __pycache__
	path = os.getcwd()
	while True:
		try:
			shutil.rmtree('%s/__pycache__' % path, ignore_errors=False, onerror=None)
		except FileNotFoundError:
			break
	print()
	os.system('pause')
	exit()
	
def main():
	os.system('cls')
	print('What would you like to do?\n1. Export Speedrun Leaderboard\n2. Export User Speedruns\n3. Exit')
	option = str(input('Select option (1, 2, 3): '))
	if option == '1':
		setupConfig()
		LeaderboardExport()
		Cleanup()
	elif option == '2':
		setupConfig()
		UserboardExport()
		Cleanup()
	elif option == '3':
		Cleanup()
	else:
		main()

try:
	from config import *
except (ModuleNotFoundError, NameError) as error:
	setupConfig()

main()
