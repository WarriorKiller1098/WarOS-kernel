# The WarOS kernel, made by WarriorKiller1098
# Features: about, shutdown, print <>, panic <>
# This is prototype 1, so there are small bugs laying around

print(" _    _            _____ _____ ")
print("| |  | |          |  _  /  ___|")
print("| |  | | __ _ _ __| | | \\ `--. ")
print("| |/\\| |/ _` | '__| | | |`--. \\")
print("\\  /\\  / (_| | |  \\ \\_/ /\\__/ /")
print(" \\/  \\/ \\__,_|_|   \\___/\\____/ ")
print("")

buildnum = 1
print("WarOS prototype " + str(buildnum) + ", do not enter numbers.")
print("")
print("Enter 'help' for more info.")
while True:
    cinput = input("kernel:>").strip()
    if cinput == "about":
        print("WarOS, prototype " + str(buildnum))
    elif cinput == "shutdown":
        print("Shutting down", end="")
        for i in range(3):
            print(".", end="")
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
        print("about, shutdown, print <>, panic <>")
    elif cinput.startswith("panic"):
        paniclog = cinput[len("panic"):]
        print("")
        print("KernelPanic")
        print("The WarOS kernel has panicked!")
        if paniclog != "":
            print("Error code:" + paniclog)
        break
    else:
        print("Command " + cinput + " does not exist")