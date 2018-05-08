import urllib.request
import json
import os

def VariableIDtoName(parentvariableID):
	while True:
		# Read game name
		
		Variables = dict()
		varList = str()
		
		try:
			variableID_url = 'https://www.speedrun.com/api/v1/variables/%s' % parentvariableID
			response = urllib.request.urlopen(variableID_url).read()
			obj = str(response, 'utf-8')
			data = json.loads(obj)

			parentName = data['data']['name']
			count = 1
			for item in data['data']['values']['choices']:
				varList += data['data']['values']['choices'][item] + '\n'
				count += 1
			Variables[parentName] = varList
			print(Variables)
			os.system('pause')
			return childVariables
		except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
			print("Parent Variable ID Error...\n", e)
			os.system('pause')
			continue

def IDtoGame(game_id):
	while True:
		# Read game name
		try:
			game_url = 'https://www.speedrun.com/api/v1/games/%s' % game_id
			response_game = urllib.request.urlopen(game_url).read()
			game_obj = str(response_game, 'utf-8')
			game_data = json.loads(game_obj)

			gamename = game_data['data']['names']['international']
			return gamename
		except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
			print("Game ID Error...\n", e)
			os.system('pause')
			continue

def IDtoCategory(category_id):
	while True:
		# Read game name
		try:
			category_url = 'https://www.speedrun.com/api/v1/categories/%s' % category_id
			response_category = urllib.request.urlopen(category_url).read()
			category_obj = str(response_category, 'utf-8')
			category_data = json.loads(category_obj)

			category = category_data['data']['name']
			return category
		except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
			print("Game ID Error...\n", e)
			os.system('pause')
			continue
		
def IDtoName(user_ID):
	while True:
		try:
			# ID to name conversion
			api_user = 'https://www.speedrun.com/api/v1/users/%s' % (user_ID)

			response_user = urllib.request.urlopen(api_user).read()
			json_obj = str(response_user, 'utf-8')

			api_data_user = json.loads(json_obj)
			
			user_name = api_data_user['data']['names']['international']
			return user_name
		except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
			print("Name ID Error...\n", e)
			os.system('pause')
			continue

def IDtoPlatform(platform_id):
	while True:
		try:
			# ID to platform name conversion
			api_user = 'https://www.speedrun.com/api/v1/platforms/%s' % (platform_id)

			response_platform = urllib.request.urlopen(api_user).read()
			json_obj = str(response_platform, 'utf-8')

			api_data_platform = json.loads(json_obj)
			
			platform_name = api_data_platform['data']['name']
			return platform_name
		except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
			print("Platform ID Error...\n", e)
			os.system('pause')
			continue
	
def IDtoRegion(region_id):
	while True:
		if region_id == None:
			region_name = "None"
			return region_name
		else:
			try:
				# ID to region name conversion
				api_region = 'https://www.speedrun.com/api/v1/regions/%s' % (region_id)

				response_region = urllib.request.urlopen(api_region).read()
				json_obj = str(response_region, 'utf-8')

				api_data_region = json.loads(json_obj)
				
				region_name = api_data_region['data']['name']
				return region_name
			except (NameError, urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
				print("Region ID Error...\n", e)
				os.system('pause')
				continue

def secToTime(sec):
	if sec >= 3600:
		m, s = divmod(sec, 60)
		h, m = divmod(m, 60)
		return "%d:%02d:%s" % (h, m, round(s, 3))
	elif sec < 3600:
		m, s = divmod(sec, 60)
		return "%d:%s" % (m, round(s, 3))
	else:
		return "Time Error..."