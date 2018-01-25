## Made by TimeTravelPenguin
## Check for updates at https://github.pengu.space
## Or simply visit https://pengu.space for more general stuff

import urllib.request
import json
import os
import datetime
import time
import math

#Set title and clock
os.system("title Loading game data...")
os.system('chcp 65001')

start = time.time()
time.clock()
elapsed = 0

os.system('cls')

####################################################################

#Set game information
user = 'timetravelpenguin'
game = 'smo'
category = 'any'
#Query should be '?conditionA=1&condintionB=2&conditionC=3'
query = '?emulators=false'

####################################################################

#Leaderboard URL
api_url = 'https://www.speedrun.com/api/v1/leaderboards/%s/category/%s%s' % (game, category, query)

#Start up text
print("This python script was written and coded by TimeTravelPenguin")
print()
print("For more, goto: https://pengu.space")
print()

#read game name

try:
	game_url = 'https://www.speedrun.com/api/v1/games/%s' % game
	response_game = urllib.request.urlopen(game_url).read()
	game_obj = str(response_game, 'utf-8')
	game_data = json.loads(game_obj)

	gamename = game_data['data']['names']['international']
except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as error:
	os.system('cls')
	print("Error...")
	print("Please check your Internet connection, and that your game, category, etc. settings are correct...")
	print()
	os.system('pause')
	exit()
		
	
#os.system('cls')

#Initial information display
os.system("title Connecting to API...")

time_var = datetime.datetime.now()
print("==========================================================================")
print()
print(time_var)
print('\nGame: %s (%s)' % (gamename, game))
print('Category: ' + category)
print()

#Load leaderboard API
response = urllib.request.urlopen(api_url).read()
json_obj = str(response, 'utf-8')

api_data = json.loads(json_obj)

file = open("API_export_%s_%s.txt" % (game, category), 'w', encoding='utf-8')

file.write('%s\n\n' % time_var)

#ID to name conversion
def IDtoName(name_id):
	api_user = 'https://www.speedrun.com/api/v1/users/%s' % (name_id)

	response_user = urllib.request.urlopen(api_user).read()
	json_obj = str(response_user, 'utf-8')

	api_data_user = json.loads(json_obj)
	
	user_name = api_data_user['data']['names']['international']
	return user_name

def secToMin(sec):
	m, s = divmod(sec, 60)
	return "%d:%s" % (m, round(s, 3))
	
#title information for time and percentage	
max_runs = len(api_data['data']['runs'])
count = 0
errors = 0

#list leaderboard data
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
print("Completed Successfully with %s errors..." % str(errors))
os.system('pause')
exit()