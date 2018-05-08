import datetime
import os
import urllib.request
from itertools import chain
from scripts import startup
from scripts import apiConnect
from scripts import converters as conv
from scripts import APIthreads
from scripts import write

def SpeedrunLeaderboard(game, category, query):
	dict_SortedNames = dict()
	dict_Users = dict()
	
	startup.startText()
	
	gamename = conv.IDtoGame(game)
	os.system('title Speedrun Leaderboard Exporter (SLE)')
	
	time_var = datetime.datetime.now()
	print(time_var)
	
	print('\nGame: %s (%s)' % (gamename, game))
	print('Category: ' + category)
	if query == '':
		print('Query: None')
	else:
		print('Query: ' + query)

	print('\nDownloading Speedrun Leaderboard...')
	
	# Load API
	api = apiConnect.SpeedrunLeaderboard(game, category, query)

	dict_ID, dict_Guest, dict_Place, dict_Time = getSL(api)
	
	max_runs = len(api['data']['runs'])
	
	print('Fetching Usernames...')
	names = APIthreads.IDThread(dict_ID)
	
	for key, value in names.items():
		dict_Users[key] = '%s\t%s\t%s' % (dict_Place[key], value, dict_Time[key])

	for key, value in sorted(chain(dict_Users.items(), dict_Guest.items())):
		dict_SortedNames[key] = value

	write.WriteFile_SL(dict_SortedNames)
	
def getSL(api):
	counter = 1
	errors = 0
	dict_ID = dict()
	dict_Guest = dict()
	dict_Place = dict()
	dict_Time = dict()
	
	for item in api['data']['runs']:
		place = item['place']
		runtime = item['run']['times']['primary_t']
		
		try:
			username = item['run']['players'][0]['id']
			dict_ID[counter] = '%s' % (username)
			dict_Place[counter] = place
			dict_Time[counter] = runtime
		except KeyError:
			username = item['run']['players'][0]['name']
			dict_Guest[counter] = '%s\t%s\t%s' % (place, username, runtime)
		except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as error:
			print("Error...", error)
			errors += 1
			continue
		counter += 1
	
	return dict_ID, dict_Guest, dict_Place, dict_Time
		

def UserSpeedruns(username):
	dict_SortedNames = dict()
	dict_Users = dict()
	
	startup.startText()
	
	username = conv.IDtoName(username)
	os.system('title Speedrun Leaderboard Exporter (SLE)')
	
	time_var = datetime.datetime.now()
	print(time_var)
	
	print('\nUser: %s' % username)

	print('\nDownloading Speedrun Leaderboard...')
	
	# Load API
	api = apiConnect.UserSpeedruns(username)

	max_runs = int(len(api['data']))
	
	print('Fetching Speedruns...\n')
	userdata = getUS(api)
	
	write.WriteFile_UL(userdata)
	
def getUS(api):
	dict_user = dict()
	
	place = dict()
	game_id = dict()
	category_id = dict()
	runtime = dict()
	platform_id = dict()
	region_id = dict()
	emulated = dict()

	# List leaderboard data
	count = 1
	for item in api['data']:
		try:
			place[count] = item['place']
			
			game_id[count] = item['run']['game']
			category_id[count] = item['run']['category']
			runtime[count] = item['run']['times']['primary_t']
			platform_id[count] = item['run']['system']['platform']
			region_id[count] = item['run']['system']['region']
			
			emulated[count] = item['run']['system']['emulated']
			
			# dict_user[item] = "Game: %s\nPlace: %s\nCategory: %s\nRuntime: %s\nPlatform: %s\nRegion: %s\nEmulated: %s\n\n" % (game, place, category, display_runtime, platform, region, emulated)
			# print("Game: %s\nPlace: %s\nCategory: %s\nRuntime: %s\nPlatform: %s\nRegion: %s\nEmulated: %s\n\n" % (game, place, category, display_runtime, platform, region, emulated))
			
		except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as error:
			print("Error...", error)
			errors += 1
			continue
		count += 1
	userdata = APIthreads.UserThread(game_id, category_id, runtime, platform_id, region_id, place, emulated, count)		
	return userdata