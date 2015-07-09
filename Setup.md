# Requirements #

  * This script requires Windows Vista or Windows 7 (or higher) to run. It supports 32 or 64bit.
  * The script must be run as admin for it to function correctly.

# Setup #

  * Make sure you have Python 2.6 installed, you can get it at www.python.org
  * Download the script and save it to a convenient location
  * Edit the script in a text editor (I recommend Notepad++) and change the two paths in steam\_sources and steam\_target.
  * The steam\_sources variable is a list of locations where you have games you want to link into your main Steam folder. It should point to the 'steamapps' folder (or equivalent). They should be comma separated and they should each be prefixed with an 'r' like in the example.
  * The steam\_target variable is the path to your main Steam installation steamapps folder. This is usually either C:\Program Files\Steam\steamapps or C:\Program Files (x86)\Steam\steamapps if you have a 64bit OS.
  * f you have Steam running, close it now.
  * Run a command prompt as Administrator. To do this type cmd into your start menu's search box and when cmd appears, right click it and choose 'Run as Administrator'. Confirm the UAC prompt with yes.
  * ype in the path to the script - if it contains spaces encase the entire script in double quotes - followed by a space and then 'link'.
  * ress enter and the script should run and print 'All done!' with no further text.
  * eopen steam - the games should now be listed.