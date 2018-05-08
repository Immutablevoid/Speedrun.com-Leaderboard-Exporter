import urllib.request
import json

def GETdata(api_url):
	response = urllib.request.urlopen(api_url).read()
	json_obj = str(response, 'utf-8')
	api_data = json.loads(json_obj)
	return api_data

def SpeedrunLeaderboard(game, category, query):
	# Load Speedrun Leaderboard API
	api_url = 'https://www.speedrun.com/api/v1/leaderboards/%s/category/%s%s' % (game, category, query)
	api_data = GETdata(api_url)
	return api_data

def UserSpeedruns(user):	
	# Load User Speedruns API
	api_url = 'https://www.speedrun.com/api/v1/users/%s/personal-bests' % user
	api_data = GETdata(api_url)
	return api_data
	
def getCategoryVariables(category):
	# Get list of Variable Parents
	api_url = 'https://www.speedrun.com/api/v1/categories/%s/variables' % category
	api_data = GETdata(api_url)
	return api_data
	
def getCategories(game):
	# Get list of Categories for a game
	api_url = 'https://www.speedrun.com/api/v1/games/%s/categories' % game
	api_data = GETdata(api_url)
	return api_data