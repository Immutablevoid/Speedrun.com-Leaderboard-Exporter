# Speedrun.com Leaderboard Exporter (SLE)

SLE is a Python script that exports basic leaderboard information for data analysis.
It helps to aid in the documentation of speedruns at a given time from speedrun.com

## How to use

To export a speedrun's leaderboard from speedrun.com, you must first configure the GameData.py file.
It's very simple, and I will provide you a basic guide on how to modify your script to export any leaderboard.

Firstly, open the GameData.py script by opening it in your prefered text editor.
Personally, I suggest [Notepad++](https://notepad-plus-plus.org/download/) for it's built-in syntax.

If the file doesn't exist, run SLE.py, and it will create a premade file for you, before closing.
You can then edit the necessary fields in the file.

Once opened, it should show:

```
# Set game information
# username / ID
# user = 'y8dwlrgj'
user = 'timetravelpenguin'
game = 'smo'
category = '100'

# Query should be '?conditionA=1&condintionB=2&conditionC=3'
# For more query filter options, visit:
# https://github.com/speedruncomorg/api/blob/master/version1/runs.md#get-runs

# For no filter, query = ''
query = '?emulators=false'
```

Here you can modify the target user, game, the category, and any query you wish to apply.
This is where a little bit of research and knowledge come in. Locate your speedrun leaderboard on the speedrun.com website, and find the game's ID. This is in the URL. Here I have *SMO* for Super Mario Odyssey, or, https://www.speedrun.com/smo.

Similary, you need to find the category ID by doing a similar method. Once on the website, click on the category and find it in the URL. For example:
* https://www.speedrun.com/smo#Any	-> category = 'any'
* https://www.speedrun.com/smo#100	-> category = '100'
* https://www.speedrun.com/smo#All_Missions	-> category = 'All_Missions'

Note that some leaderboards can be a little funky due to how they have been set up, and filtering may be a neccisary requirement for optimal results. For more information about query types, check it out [here](https://github.com/speedruncomorg/api/blob/master/version1/runs.md#get-runs).

When you start up SLE.py, you will be presented with this screen:
```
What would you like to do?
1. Export Speedrun Leaderboard
2. Export user speedruns
3. Exit
Select option (1, 2, 3):
```

Option 1 will export the leaderboard of *game* for *category*. It will also apply the query.
Option 2 will list and export all the speedruns (personal bests) by *user*.

More information can be found by looking into the speedrun.com API, which can be found [here](https://github.com/speedruncomorg/api).

## Once exported

Once the script is completed, you will have a .txt file with each line containing something similar to [this](https://github.com/TimeTravelPenguin/Speedrun.com-Leaderboard-Exporter/blob/master/ExampleFiles/SLE_Export_smo_Darker_Side.txt):
```
Year-Month-Day Hour:Minute:Second

1	user	time
2	user	time
3	user	time
4	user	time
...

Completed Successfully with 0 errors...
```

or [this](https://github.com/TimeTravelPenguin/Speedrun.com-Leaderboard-Exporter/blob/master/ExampleFiles/SLE_Export_timetravelpenguin.txt):
```
2018-01-26 19:15:05.681257

Place: 412
Game: Super Mario Odyssey
Runtime: 4796
Platform: Switch
Region: EUR / PAL
Emulated: False

Place: 247
Game: Super Mario 64
Runtime: 1246
Platform: Nintendo 64
Region: USA / NTSC
Emulated: True

Place: 470
Game: Super Mario 64
Runtime: 1556
Platform: Nintendo 64
Region: EUR / PAL
Emulated: False

Place: 26
Game: Pokémon Emerald
Runtime: 20464
Platform: Game Boy Advance
Region: None
Emulated: True


Completed Successfully with 0 errors...
```


Each line has each data separated by a tab space, allowing for an easy copy/paste into spreadsheets (e.g. Microsoft Excel), for easy graphing, or analysis. It also shows you the number of errors that occured during export. This will likely be due to a timeout error, and if this occures, the script will automatically repeat until successful (hopefully).

## Downloading

The latest release can be downloaded from the [Releases Page](https://github.com/TimeTravelPenguin/Speedrun.com-Leaderboard-Exporter/releases). From here, the .zip file of recent build can be found. The files can then be extracted and opened.

## Requirements

As of the current build, it has the following system requirements:

* Currently requires Windows
* [Python 3.0](https://www.python.org/downloads/) or later

## Minor note

The script may take a while to export, depending on the size of the leaderboard.
Due to the way the API works, the script has a lot of trouble finding the "username" of a speedrunner.

On speedrun.com they use "user IDs", rather than "user names" on each leaderboard. So the script has to manually goto each player's URL and find their unsername. User ID's are messy. For example, my username is *TimeTravelPenguin*, but my user ID is *y8dwlrgj*.

Because of this, the script has to manually find each user ID's user name, and that is unfortunately slightly slow.
