# mac_address_changer

Getting the value for  the interface and mac addr to a variable and
then pass the value to the command directly
secure code
handling user input if the user put ; or && to execute another command
it will stop by removing the shell=True single string commmand
rather we remove the shell=True and exec the computer and get command
in a list variable one by one which will avoid this user-input manipulation

we can give value in as a argument in a command line using sys modules
or with an option with help and switch we use optparse module
python macchanger.py --interface wlan0 --mac 11:aa:dd:ff:gg:hh
python macchanger.py --help to print help
# init the parser object
# adding the options like -i or --interface switches, dest this where the passed values get saved and help display the help msg python macchanger.py --help
# the funtion returns a value to this 2 varible options and arguments
# options is nobut the wlan0 and aa:bb:cc:dd:ee:ff
# arguments is nothingbut --interface and --mac or -i and -m
# options contains the value to get the value we call options.interface and options.new_mac
