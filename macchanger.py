#!/usr/bin/python
'''
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
#init the parser object
#adding the options like -i or --interface switches, dest this where the passed values get saved and help display the help msg python macchanger.py --help
#the funtion returns a value to this 2 varible options and arguments
#options is nobut the wlan0 and aa:bb:cc:dd:ee:ff
#arguments is nothingbut --interface and --mac or -i and -m
#options contains the value to get the value we call options.interface and options.new_mac
'''

import subprocess
import optparse
import re


def macchanger(interface, macaddr):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", macaddr])
    subprocess.call(["ifconfig", interface, "up"])

    print("[+] Changing Mac Address of Interface %s to %s" % (interface, macaddr))


def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="add new mac address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Specify an Interface use python macchanger --help for more details")
    elif not options.new_mac:
        parser.error("[-] Specify an MacAddr use python macchanger --help for more details")

    return options


def getmac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    current_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if current_mac:
        return current_mac.group(0)
    else:
        return None


options = get_argument()
macchanger(options.interface, options.new_mac)
final_mac = getmac(options.interface)

if final_mac == options.new_mac:
    print("Mac Address Successfully Changed with new one %r" % final_mac)
else:
    print("Error occurred Fix It")
