--------------------
RpiTemplogger Readme
--------------------

01/16/13

Templogger consists of a shell script which generates a log file and a python script which analyzes the generated logfile and gives a report with statistics such as the Highest Temperature, Lowest Temperature and Average Temperature of the Raspberry Pi.

This is a very rough piece of code at the moment. Tested with Raspbian Wheezy.

Usage:

Place the shell script in a directory e.g. /home/pi/bin and add edit your crontab (crontab -e) to run it as often as you want.

E.G. To have it run every half an hour add the following line to the bottom on your crontab:

0,30 * * * * /home/pi/bin/templogger.sh

The script will add a line with the current Time, Date and Temperature (in the format of HH-MM-SS:MM-DD-YY:TEMP) to the file tmplog.

Now run the templogoutput.py file to generate a report based on the data contained in the log file.





 
