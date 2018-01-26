## Made by TimeTravelPenguin
## Check for updates at https://github.pengu.space
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

os.system('cls') 
# Check if GameData.py exists
if os.path.isfile('GameData.py') == True:
	pass
elif os.path.isfile('GameData.py') == False:
	print('GameData.py not found... Creating new file...')
	varDir = open("GameData.py", 'w', encoding='utf-8')
	msg = "# Set game information\n# username / ID\n# user = \'y8dwlrgj\'\nuser = \'timetravelpenguin\'\ngame = \'smo\'\ncategory = \'100\'\n\n# Query should be \'?conditionA=1&condintionB=2&conditionC=3\'\n# For more query filter options, visit:\n# https://github.com/speedruncomorg/api/blob/master/version1/runs.md#get-runs\n\n# For no filter, query = \'\'\nquery = \'?emulators=false\'\n"
	varDir.write(msg)
	varDir.close()
	print('Please edit GameData.py, and then rerun SLE.py...\n')
	os.system('pause')
	exit()

from GameData import *

def LeaderboardExport():
	# Leaderboard URL
	api_url = 'https://www.speedrun.com/api/v1/leaderboards/%s/category/%s%s' % (game, category, query)

	# Start up text
	print("This python script was written and coded by TimeTravelPenguin")
	print()
	print("For more, goto: https://SLE.pengu.space")
	print()

	os.system("title Connecting to API...")
	gamename = IDtoGame(game)

	time_var = datetime.datetime.now()
	print("==========================================================================")
	print()
	print(time_var)
	print('\nGame: %s (%s)' % (gamename, game))
	print('Category: ' + category)
	if query == '':
		print('Query: None')
	else:
		print('Query: ' + query)
	print()

	# Load leaderboard API
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
		while True:
				try:
					place = item['place']
					runtime = item['run']['times']['primary_t']
					name_id = item['run']['players'][0]['id']
					user_name = IDtoName(name_id)
					print(place, user_name, runtime)
					file.write("%s\t%s\t%s\n" % (place, user_name, runtime))
				except KeyError:
					name_id = item['run']['players'][0]['name']
					print(place, name_id, runtime)
					file.write("%s\t%s\t%s\n" % (place, name_id, runtime))
					break
				except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as error:
					print("Error...")
					errors += 1
					continue
				break
		count += 1
		percent = str(round(count * 100 / max_runs, 3))
		fract = "%s/%s" % (count, max_runs) 
		elapsed = secToMin(time.time() - start)
		etaTime = secToMin((time.time() - start) * (max_runs / count - 1))
		os.system("title Progress: " + percent + "% (" + fract + ")   Time: " + str(elapsed) + "   Errors: " + str(errors) + "   ETA: " + etaTime)
	file.write("\nCompleted Successfully with %s errors...\n" % errors)
	file.close()
	print()
	print("Completed Successfully with %s errors...\n" % str(errors))
	os.system('pause')

def UserboardExport():	
	# Leaderboard URL
	api_url = 'https://www.speedrun.com/api/v1/users/%s/personal-bests' % user

	# Start up text
	print("This python script was written and coded by TimeTravelPenguin")
	print()
	print("For more, goto: https://SLE.pengu.space")
	print()
	
	# Initial information display
	os.system("title Connecting to API...")

	username = IDtoName(user)
	
	time_var = datetime.datetime.now()
	print("==========================================================================")
	print()
	print(time_var)
	print('\nUser: %s\n' % username)
	

	# Load leaderboard API
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
					runtime = item['run']['times']['primary_t']
					platform_id = item['run']['system']['platform']
					platform = IDtoPlatform(platform_id)
					region_id = item['run']['system']['region']
					region = IDtoRegion(region_id)
					emulated = item['run']['system']['emulated']
					print("Place: %s\nGame: %s\nRuntime: %s\nPlatform: %s\nRegion: %s\nEmulated: %s\n" % (place, game, runtime, platform, region, emulated))
					file.write("Place: %s\nGame: %s\nRuntime: %s\nPlatform: %s\nRegion: %s\nEmulated: %s\n\n" % (place, game, runtime, platform, region, emulated))
				except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as error:
					print("Error...")
					errors += 1
					continue
				break
		count += 1
		percent = str(round(count * 100 / max_runs, 3))
		fract = "%s/%s" % (count, max_runs) 
		elapsed = secToMin(time.time() - start)
		etaTime = secToMin((time.time() - start) * (max_runs / count - 1))
		os.system("title Progress: " + percent + "% (" + fract + ")   Time: " + str(elapsed) + "   Errors: " + str(errors) + "   ETA: " + etaTime)
	file.write("\nCompleted Successfully with %s errors...\n" % errors)
	file.close()
	print()
	print("Completed Successfully with %s errors...\n" % str(errors))
	os.system('pause')
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
		os.system('cls')
		print("Game ID Error...")
		print("Please check your Internet connection, and that GameData.py has correct information")
		print()
		os.system('pause')
	
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
		os.system('cls')
		print("Name ID Error...")
		print("Please check your Internet connection...")
		print()
		os.system('pause')

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
		os.system('cls')
		print("Platform ID Error...")
		print("Please check your Internet connection...")
		print()
		os.system('pause')
	
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
			os.system('cls')
			print("Region ID Error...")
			print("Please check your Internet connection...")
			print()
			os.system('pause')

def secToMin(sec):
	m, s = divmod(sec, 60)
	return "%d:%s" % (m, round(s, 3))

def Cleanup():
	# Delete __pycache__
	path = os.getcwd()
	try:
		shutil.rmtree('%s/__pycache__' % path, ignore_errors=False, onerror=None)
	except FileNotFoundError:
		pass
	exit()
	
def main():
	os.system('cls')
	print('What would you like to do?\n1. Export Speedrun Leaderboard\n2. Export user speedruns\n3. Exit')
	option = int(input('Select option (1, 2, 3): '))
	if option == 1:
		os.system('cls')
		LeaderboardExport()
		Cleanup()
	elif option == 2:
		os.system('cls')
		UserboardExport()
		os.system('pause')
		Cleanup()
	elif option == 3:
		Cleanup()
		exit()
	else:
		main()

main()
