import threading
from gevent.pool import Pool
import gevent.monkey
from scripts import converters as conv

dict_Names = dict()
dict_Game = dict()
dict_Category = dict()
dict_Runtime = dict()
dict_Platform = dict()
dict_Region = dict()

def getName(key, value):
	dict_Names[key] = conv.IDtoName(value)
	
def getGame(key, game):
	dict_Game[key] = conv.IDtoGame(game)

def getCategory(key, category):
	dict_Category[key] = conv.IDtoCategory(category)
	
def getTime(key, runtime):	
	dict_Runtime[key] = conv.secToTime(runtime)
	
def getPlatform(key, platform):
	dict_Platform[key] = conv.IDtoPlatform(platform)
	
def getRegion(key, region):
	dict_Region[key] = conv.IDtoRegion(region)
	
def IDThread(dict_ID):
	for key, value in dict_ID.items():
		t = threading.Thread(target=getName, args=(key, value,))
		t.start()
	t.join()	
	return dict_Names

def UserThread(game, category, runtime, platform, region, place, emulated, count):
	gevent.monkey.patch_all()
	pool = gevent.pool.Pool()
	for i in range(1, count):
		pool.spawn(getGame, i, game[i])
		pool.spawn(getCategory, i, category[i])
		pool.spawn(getTime, i, runtime[i])
		pool.spawn(getPlatform, i, platform[i])
		pool.spawn(getRegion, i, region[i])

	pool.join()

	UserDict = dict()
	for i in range(1, count):
		UserDict[i] = "Game: %s\nPlace: %s\nCategory: %s\nRuntime: %s\nPlatform: %s\nRegion: %s\nEmulated: %s\n\n" % (dict_Game[i], place[i], dict_Category[i], dict_Runtime[i], dict_Platform[i], dict_Region[i], emulated[i])
	return UserDict