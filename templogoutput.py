## Raspberry Pi Temperature Log Analyzer - 2013 Jamie Aitken.

import datetime
import socket
hostname = socket.gethostname()
now = datetime.datetime.now()
nowtime = now.strftime('Y-%m-%d %H:%M')
file = open('/tmp/logs/templog', 'r')
outfile = open('/home/pi/log/templog', 'w')
templist = []
temp = []
line = file.readline()
info = ['Date: ', 'Time: ', 'Temperature: ']



while line != '':
        
        line = line.rstrip('\n')
        templist.append(line)
        line = file.readline()
	
	
file.close	

def initializetemps():
        sublist = []
        x = 0
        while x < len(templist):
                sublist = []
                data = templist[x]
                date = data.split(":")[1]
                sublist.append(date)
                time = data.split(":")[0]
                sublist.append(time)
                temps = float(data.split(":")[2])
                sublist.append(temps)
                temp.append(sublist)
                x = x + 1

def latestreading():
    global latesttemp
    global latesttime
    latesttemp = temp[len(temp) - 1][2]
    latesttime = temp[len(temp) -1][1]

def lastfive():
    global lastfi
    global lastfo
    global lastth
    global lasttw
    global laston
    lastfi = temp[len(temp) -2]
    lastfo = temp[len(temp) -3]
    lastth = temp[len(temp) -4]
    lasttw = temp[len(temp) -5]
    laston = temp[len(temp) -6]

def printdatetemp():
        y = 0
        while y < len(temp):
                z = 0
                while z < len(temp[y]):
                        print(info[z], temp[y][z])
                        z = z + 1
                y = y + 1
                
def averagetemp():
        global avg
        i = 0
        avg = 0.0
        while i < len(temp):
                avg = avg + temp[i][2]
                i = i + 1
        avg = round((avg / len(temp)),1)
        

def showmax():
        i= 0
        templist = []
        global maxnum
        global minnum
        while i < len(temp):
                templist.append(temp[i][2])
                i = i + 1
        maxnum = max(templist)
        minnum = min(templist)
                

def writeout():
    outfile.write('\n---------------------------------------------------\n')
    outfile.write('Temperature Log Report for ' + str(hostname) + '\n')
    outfile.write('---------------------------------------------------\n\n')
    outfile.write('Report Generated: ' + str(now) +'\n')
    outfile.write('Log Created: ' + str(temp[0][1]) + '\n\n')
    outfile.write('Latest Temperature (' + str(latesttime) + '): ' + str(latesttemp) + ' Clesius\n')
    outfile.write('Highest Recorded Temperature: ' + str(maxnum) + ' Celsius\n')
    outfile.write('Lowest Recorded Temperature: ' + str(minnum) + ' Celsius\n')
    outfile.write('Average Temperature: ' + str(avg) + ' Celsius\n\n')
    outfile.write('Previous Five Temperatures:\n')
    outfile.write(str(lastfi[1]) + ' ' + str(lastfi[2]) + ' Celsius\n')
    outfile.write(str(lastfo[1]) + ' ' + str(lastfo[2]) + ' Celsius\n')
    outfile.write(str(lastth[1]) + ' ' + str(lastth[2]) + ' Celsius\n')
    outfile.write(str(lasttw[1]) + ' ' + str(lasttw[2]) + ' Celsius\n')
    outfile.write(str(laston[1]) + ' ' + str(laston[2]) + ' Celsius\n')
    outfile.close()

print('Generating Logfile...')
initializetemps()
latestreading()
averagetemp()
lastfive()
showmax()
writeout()
print('Logfile Generation Complete.')
