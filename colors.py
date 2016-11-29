
class bcolors:
	green = '\033[92m'
	endc = '\033[0m'
	pink = '\033[95m'
	blue = '\033[94m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	
hr = '===================='

print(bcolors.green + hr + ' green ' + hr + bcolors.endc)
print(bcolors.pink + hr + ' pink ' + hr + bcolors.endc)
print(bcolors.blue + hr + ' blue ' + hr + bcolors.endc)
print(bcolors.yellow + hr + ' yellow ' + hr + bcolors.endc)
print(bcolors.red + hr + ' red ' + hr + bcolors.endc)
print(bcolors.bold + hr + ' bold ' + hr + bcolors.endc)
print(bcolors.underline + hr + ' underline ' + hr + bcolors.endc)
