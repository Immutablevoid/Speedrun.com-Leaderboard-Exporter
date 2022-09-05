import datetime
import os
import urllib.request
from itertools import chain
from scripts import startup
from scripts import apiConnect
from scripts import converters as conv
from scripts import APIthreads
from scripts import write
from scripts import main

def getCategories(game):
	os.system('title Speedrun Leaderboard Exporter (SLE)')
	os.system('cls')
	
	RAWcategories = dict()
	PARSEcategories = dict()
	
	fullGameName = conv.IDtoGame(game)
	
	print('Choose a category from the game: %s\n' % fullGameName)
	print('Categories:')
	
	categories = dict()
	
	# Get categories as dict {Name:ID}
	category_api = apiConnect.getCategories(game)
	
	max_categories = 0
	for item in category_api['data']:
		max_categories += 1
		RAWcategories[max_categories] = item['id']
		PARSEcategories[max_categories] = item['name']
	return RAWcategories, PARSEcategories, max_categories, fullGameName

def getCategoryVariables(category):
	# Get list of Variable Parent IDs
	RAWParentVariables = dict()
	PARSEDParentVariables = dict()
	RAWChildVariables = dict()
	PARSEDChildVariables = dict()
	ChildVariables = dict()
	
	api = apiConnect.getCategoryVariables(category)
	
	count = 0
	for item in api['data']:
		count += 1
		RAWParentVariables[count] = item['id']
		PARSEDParentVariables[count] = item['name']

	max_categories = 0
	parentCount = 0 
	for i in range(len(api['data'])):
		children = str()
		parentCount += 1
		for item in api['data'][i]['values']['choices']:
			max_categories += 1
			RAWChildVariables[max_categories] = item
			PARSEDChildVariables[max_categories] = api['data'][i]['values']['choices'][item]
			children += '(%s) %s\n' % (item, api['data'][i]['values']['choices'][item])
		ChildVariables[parentCount] = children
	
	return RAWParentVariables, PARSEDParentVariables, ChildVariables, parentCount

def FindVariables(game, RAWcategories, PARSEcategories, max_categories, fullGameName):
	for i in range(1, max_categories + 1):print('%s. (%s) %s' %(i, RAWcategories[i], PARSEcategories[i]))
	
	while True:
		option = str(input('\nOption: '))
		try:
			if int(option) in range(1, max_categories + 1):
				category = RAWcategories[int(option)]
				break
		except ValueError:
			pass	
	
	RAWParentVariables, PARSEDParentVariables, ChildVariables, max_categories = getCategoryVariables(category)
	
	os.system('cls')
	
	print('For %s - (%s) %s, the variables are:' %(fullGameName, category, PARSEcategories[int(option)]))
	for i in range(1, max_categories + 1):
		print('(%s) %s:\n%s' % (RAWParentVariables[i], PARSEDParentVariables[i], ChildVariables[i]))
	
	os.system('pause')
	main.main()

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

	dict_ID, dict_Guest, dict_Place, dict_Time, dict_Link = getSL(api)
	
	max_runs = len(api['data']['runs'])
	
	print('Fetching Usernames...')
	names = APIthreads.IDThread(dict_ID)
	
	for key, value in names.items():
		dict_Users[key] = '%s,%s,%s,%s' % (dict_Place[key], value, dict_Time[key], dict_Link[key])

	for key, value in sorted(chain(dict_Users.items(), dict_Guest.items())):
		dict_SortedNames[key] = value

	write.WriteFile_SL(dict_SortedNames, game, category)
	
def getSL(api):
	counter = 1
	errors = 0
	dict_ID = dict()
	dict_Guest = dict()
	dict_Place = dict()
	dict_Time = dict()
	dict_Link = dict()
	
	for item in api['data']['runs']:
		print(item)
		place = item['place']
		runtime = item['run']['times']['primary_t']
		link = item['run']['videos']['links'][0]['uri']
		
		try:
			username = item['run']['players'][0]['id']
			dict_ID[counter] = '%s' % (username)
			dict_Place[counter] = place
			dict_Time[counter] = str(datetime.timedelta(0, runtime))
			dict_Link[counter] = link
		except KeyError:
			username = item['run']['players'][0]['name']
			dict_Guest[counter] = '%s,%s,%s,%s' % (place, username, runtime, link)
		except (TimeoutError, urllib.error.URLError, urllib.error.HTTPError) as error:
			print("Error...", error)
			errors += 1
			continue
		counter += 1
	
	return dict_ID, dict_Guest, dict_Place, dict_Time, dict_Link
		

def UserSpeedruns(user):
	dict_SortedNames = dict()
	dict_Users = dict()
	
	startup.startText()
	
	username = conv.IDtoName(user)
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
	
	write.WriteFile_UL(userdata, username)
	
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