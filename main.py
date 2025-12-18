# The WarOS kernel, made by WarriorKiller1098
# Features: about, shutdown, print <>, panic <>
# This is prototype 15, so there are small bugs laying around

import requests
import time
import os

buildnum = 15

def boot(waiting):
	print(" _    _            _____ _____ ")
	print("| |  | |          |  _  /  ___|")
	print("| |  | | __ _ _ __| | | \\ `--. ")
	print("| |/\\| |/ _` | '__| | | |`--. \\")
	print("\\  /\\  / (_| | |  \\ \\_/ /\\__/ /")
	print(" \\/  \\/ \\__,_|_|   \\___/\\____/ prototype " + str(buildnum))
	print("")
	print("Loading WarOS......")
	if waiting == True:
		time.sleep(1.5)
	print("WarOS prototype " +
	str(buildnum))
	print("")
	print("Enter 'help' for more info.")

def color_blue():
	print("\033[44m\033[97m\033[2J\033[H", end="")
boot(True)

def ping(host):
	try:
		start = time.time()
		hosturl = host if host.startswith("http") else f"https://{host}"
		req = requests.get(hosturl, timeout=4)
		end = time.time()
		latency = int((end - start) * 1000)
		print(f"Reply from {host}: status={req.status_code}, time={latency}ms")
	except requests.exceptions.Timeout:
		print(f"Ping timed out.")
	except requests.exceptions.ConnectionError:
		print(f"Cannot reach {host}.")
	except Exception as e:
		print(f"Ping failed! :(: {e}")
while True:
    cinput = input("kernel:>").strip()
    if cinput == "about":
        print("WarOS, prototype " + str(buildnum))
    elif cinput == "shutdown":
        print("Shutting down..", end="")
        break
    elif cinput.startswith("print"):
        text = cinput[len("print"):]
        if text == "":
            print("There's nothing to print. Please enter something after 'print'.")
        else:
            print(text.strip())
    elif cinput == "help":
        print("'<>' stands for something you'll write.")
        print("Commands are:")
        print("about, shutdown, print <>, panic <>,")
        print("color <>, clear <>, reset")
        print("")
        print("Updates:")
        print("Blue command now is a argument in color command, in prototype 10")
    elif cinput.startswith("panic"):
        paniclog = cinput[len("panic"):]
        color_blue()
        os.system("cls" if os.name == "nt" else "clear")
        print("\n\t:(")
        print("")
        print("KernelPanic")
        print("The WarOS kernel has panicked!")
        print("Please restart WarOS kernel. Fatal error has happened.. :(")
        if paniclog != "":
            print("Error code:" + paniclog)
        else:
        	print("Kernel panic happened with unknown error code.")
        while True:
        	time.sleep(1)
    elif cinput.startswith("clear"):
    	parts = cinput.split()
    	args = parts[1:]
    	if "--help" in args:
    		print("By default it waits 1 second. use 'clear notime' to remove waiting")
    		time.sleep(2)
    		continue
    	print("Clearing.. (use --help to get help.)")
    	if "notime" not in args:
    		time.sleep(1)
    	os.system("cls" if os.name == "nt" else "clear")
    	boot(True)
    elif cinput.startswith("color"):
    	colorparts = cinput.split()
    	args = colorparts[1:]
    	if "blue" in args:
    		color_blue()
    		os.system("cls" if os.name == "nt" else "clear")
    		boot(True)
    		print("Colored screen to blue.")
    	elif "--help" in args:
    		print("Type 'color blue' to color it blue!")
    		print("Also type 'reset' to reset color.")
    		print("Old blue command is now a argument in color command.")
    elif cinput == "":
    	print("Nothing has been entered.")
    elif cinput == "reset":
    	print("\033[0m", end="")
    	os.system("cls" if os.name == "nt" else "clear")
    	boot(False)
    	os.system("cls" if os.name == "nt" else "clear")
    	boot(True)
    elif cinput.startswith("ping"):
    	parts = cinput.split()
    	if len(parts) < 2:
    		print("Please enter a URL/IP after 'ping'.")
    	else:
    		ping(parts[1])
    else:
        print("Command '" + cinput + "' does not exist.")
