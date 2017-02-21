# Simple script to demo how to read a config file in Python 3

import configparser


configparser = configparser.RawConfigParser()   
configparser.read("options.cfg")


username = configparser.get('settings', 'username')
camera = configparser.get('settings', 'camera')


print ("Hello ",username)

if camera == "yes":
	print ("Camera is installed")
else:
	print ("No camera installed")


print ("End of script")

