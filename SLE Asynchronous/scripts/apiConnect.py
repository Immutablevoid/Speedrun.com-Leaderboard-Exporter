import urllib.request
import json

def SpeedrunLeaderboard(game, category, query):
	# Load Speedrun Leaderboard API
	api_url = 'https://www.speedrun.com/api/v1/leaderboards/%s/category/%s%s' % (game, category, query)
	response = urllib.request.urlopen(api_url).read()
	json_obj = str(response, 'utf-8')
	api_data = json.loads(json_obj)
	return api_data

def UserSpeedruns(user):	
	# Load User Speedruns API
	api_url = 'https://www.speedrun.com/api/v1/users/%s/personal-bests' % user
	response = urllib.request.urlopen(api_url).read()
	json_obj = str(response, 'utf-8')
	api_data = json.loads(json_obj)
	return api_data