# The WarOS kernel, made by WarriorKiller1098
# Features: about, shutdown, print <>, panic <>
# This is prototype 20, so there are small bugs laying around

import requests
import time
import os

buildnum = 20

root = os.path.dirname(os.path.abspath(__file__))

systemd = os.path.join(root, "System")
appsd = os.path.join(root, "Apps")
usersd = os.path.join(root, "Users")

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

def init_filesystem():
	for folder in [systemd, appsd, usersd]:
		if not os.path.exists(folder):
			os.makedirs(folder)
			
init_filesystem()
def ping(host):
	try:
		start = time.time()
		hosturl = host if host.startswith("http") else f"https://{host}"
		req = requests.get(hosturl, timeout=4)
		end = time.time()
		latency = int((end - start) * 1000)
		print(f"Reply from {host}: status={req.status_code}, time={latency}ms, response={req.text}")
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
        print("color <>, clear <>, reset, ping")
        print("crt, edt, del")
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
    elif cinput.startswith("crt"):
    	args = cinput.split()[1:]
    	if not args:
    		print("Please enter a filename after 'crt'.")
    		time.sleep(1)
    		continue
    	else:
    		file_name = args[0]
    		file_path = os.path.join(usersd, file_name)
    		if os.path.exists(file_path):
    			print("Overwriting is not supported.")
    		else:
    			with open(file_path, "w") as f:
    				f.write("This was written by WarOS.")
    elif cinput.startswith("edt"):
    	editparts = cinput.split()
    	
    	if len(editparts) < 2:
    		print("To edit, please enter a file path after 'edt'. ")
    		time.sleep(1)
    		continue
    	
    	file_name = editparts[1]
    	file_path = os.path.join(usersd, file_name)
    	
    	if not os.path.exists(file_path):
    		print("File does not exist!")
    		time.sleep(1)
    		continue
    	else:
    		print("\033[44m\033[97m\033[2J\033[H", end="")
    		os.system("cls" if os.name == "nt" else "clear")
    		print("WarEdit 1.0 | Editing '" + file_name + "'")
    		print("------Enter $+ to save and exit.")
    		with open(file_path, "r") as f:
    			old_lines = f.read().splitlines()
    			print("")
    			print("----old lines--------")
    			for line in old_lines:
    				print(line)
    			print("---------------------------")
    			print("")
    			new_lines = []
    			save_line = "$+"
    			
    			while True:
    				line = input("")
    				if line == save_line:
    					break
    				new_lines.append(line)
    			
    			with open(file_path, "w") as f:
    				f.write("\n".join(new_lines) + "\n")
    			os.system("cls" if os.name == "nt" else "clear")
    			print("\033[0m", end="")
    			os.system("cls" if os.name ==
    			"nt" else "clear")
    			boot(False)
    			os.system("cls" if os.name ==
    			"nt" else "clear")
    			boot(True)
    			print("File is updated successfully!")
    elif cinput == "ldir":
    	try:
    		files = os.listdir(usersd)
    		if not files:
    			print("Directory 'Users' is empty!")
    		else:
    			print("Users---------------")
    			for f in files:
    				print("File - '" + f + "'")
    	except Exception as e:
    		print("Failed to list directory: " + e)
    elif cinput.startswith("del"):
    	parts = cinput.split()
    	
    	if len(parts) < 2:
    		print("Enter a filename after 'del'.")
    		time.sleep(1)
    		continue
    	
    	file_name = parts[1]
    	file_path = os.path.join(usersd, file_name)
    	
    	if not os.path.exists(file_path):
    		print("File does not exist.")
    		time.sleep(1)
    		continue
    	
    	confirmation = input("Are you sure you want to delete '" + file_name + "'? (y/n)")
    	if confirmation == "y":
    		try:
    			os.remove(file_path)
    			print("File has been deleted!")
    		except Exception as e:
    			print("Failed to delete" + file_name + ":" + e)
    	else:
    		print("Deletion was cancelled.")
    else:
        print("Command '" + cinput + "' does not exist.")
