# Speedrun.com Leaderboard Exporter (SLE)

SLE is a basic Python script that exports basic leaderboard information for basic data analysis.
It helps to aid in the documentation of speedruns at a given time from speedrun.com

## How to use

To export a speedrun's leaderboard from speedrun.com, you must first configure a section of code in the .py script.
It's very simple, and I will provide you a basic guide on how to modify your script to export any leaderboard.

Firstly, open the .py script by right-clicking the file and opening it in your prefered tex editor.
Personally, I suggest [Notepad++](https://notepad-plus-plus.org/download/) for it's built-in syntax.

Once opened, you should located this secion in the code located near the top of the code:

```
user = 'timetravelpenguin'
game = 'smo'
category = 'any'
#Query should be '?conditionA=1&condintionB=2&conditionC=3'
query = '?emulators=false'
```

(Note: The *user* variable isn't currently used in this build, and is intended for exporting specific user's speedruns)

Here you can modify the game, the category, and any query you wish to apply.
This is where a little bit of research and knowladge come in. Locate your speedrun on the speedrun.com website, and find the game's ID. This is in the URL. Here I have *SMO* for Super Mario Odyssey, or, https://www.speedrun.com/smo.

Similary, you need to find the category ID by doing a similar method. Once on the website, click on the category and find it in the URL. For example:
* https://www.speedrun.com/smo#Any	-> category = 'any'
* https://www.speedrun.com/smo#100	-> category = '100'
* https://www.speedrun.com/smo#All_Missions	-> category = 'All_Missions'

If you do not wish to filter results, clear the query to:
```
query = ''
```
Note that some leaderboards can be a little funky due to how they have been set up, and filtering may be a neccisary requirement for optimal results. For more information about query types, check it out [here](https://github.com/speedruncomorg/api/blob/master/version1/runs.md#get-runs).

More information can be found by looking into the speedrun.com API, which can be found [here](https://github.com/speedruncomorg/api).

## Once exported

Once the script is completed, you will have a .txt file with each line containing something similar to:
```
Year-Month-Day Hour:Minute:Second

1	user	time
2	user	time
3	user	time
4	user	time
...

Completed Successfully with 0 errors...
```
Each line has each data separated by a tab space, allowing for an easy copy/paste into spreadsheets (e.g. Microsoft Excel), for easy graphing, or analysis. It also shows you the number of errors that occured during export. This will likely be due to a timeout error, and if this occures, the script will automatically repeat until successful (hopefully).

## Downloading

The latest release can be downloaded from our [Releases Page](https://github.com/TimeTravelPenguin/Speedrun.com-Leaderboard-Exporter/releases). From here .zip files of recent builds can be found. The files can then be extracted and opened.

## Requirements

As if the current build, it has the following system requirements:

[Python 3.0](https://www.python.org/downloads/) or later
