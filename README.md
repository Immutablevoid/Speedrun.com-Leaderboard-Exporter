# Speedrun.com Leaderboard Exporter (SLE)

SLE is a program that exports basic speedrun.com leaderboard information for data analysis.
It helps to aid in the documentation of speedruns at a given time from speedrun.com

## How to use

To export a speedrun's leaderboard from speedrun.com, simply run the program, edit the setting, and click the appropriate buttons.

Here you can modify the target user, game, the category, and any query you wish to apply.
This is where a little bit of research and knowledge come in. Locate your speedrun leaderboard on the speedrun.com website, and find the game's ID. This is in the URL. An example would be *SMO* for Super Mario Odyssey, or, https://www.speedrun.com/smo.

Similary, you need to find the category ID by doing a similar method. Once on the website, click on the category and find it in the URL. For example:
* https://www.speedrun.com/smo#Any	-> category = 'any'
* https://www.speedrun.com/smo#100	-> category = '100'
* https://www.speedrun.com/smo#All_Missions	-> category = 'All_Missions'

You can also modify the setting to display and/or export in either seconds of a formatted time such as H:MM:SS.
Leaving the export in seconds makes spredsheeting easier, and having the display as H:MM:SS makes it easier to read whilst on-screen (aesthetics).

Note that some leaderboards can be a little funky due to how they have been set up, and filtering may be a neccisary requirement for optimal results. For more information about query types, check it out [here](https://github.com/speedruncomorg/api/blob/master/version1/runs.md#get-runs).

More information can be found by looking into the speedrun.com API, which can be found [here](https://github.com/speedruncomorg/api).

## Statistics mode

If exporting a leaderboard, you will be asked if you wish to use Statistics mode, or not. Setting this option will make the program skip over finding the speedrunners names when exporting a Leaderboard. While set, the export should finish within several seconds, rather than several to many minutes.

## Once exported

Once the script is completed, you will have a .csv file with each line containing something similar to [this](https://github.com/TimeTravelPenguin/Speedrun.com-Leaderboard-Exporter/blob/master/ExampleFiles/SLE_Export_smb1_any.csv)

Each line has each data separated by a tab space, allowing for an easy import into spreadsheets (e.g. Microsoft Excel), for easy graphing, or analysis

## Downloading

The latest release can be downloaded from the [Releases Page](https://github.com/TimeTravelPenguin/Speedrun.com-Leaderboard-Exporter/releases). From here, the .zip file of recent build can be found. The files can then be extracted and opened.

## Requirements

As of the current build, it has the following system requirements:

* .NET Framework 3.5 SP1

## Minor note

The script may take a while to export, depending on the size of the leaderboard.
Due to the way the API works, the script has a lot of trouble finding the "username" of a speedrunner.

On speedrun.com they use "user IDs", rather than "user names" on each leaderboard. So the script has to manually goto each player's URL and find their unsername. User ID's are messy. For example, my username is *TimeTravelPenguin*, but my user ID is *y8dwlrgj*.

Because of this, the script has to manually find each user ID's user name, and that is unfortunately slightly slow.
