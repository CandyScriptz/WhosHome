#!/usr/bin/python3
#Created by CandyScriptz

import time
from socket import *
import sys
import os

black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'
startTime = time.time()

print(black("========================================================"))
intro = """
 #   #  #                    #   #                      
 #   #  #                    #   #                      
 #   #  # ##    ###    ###   #   #   ###   ## #    ###  
 # # #  ##  #  #   #  #      #####  #   #  # # #  #   # 
 # # #  #   #  #   #   ###   #   #  #   #  # # #  ##### 
 ## ##  #   #  #   #      #  #   #  #   #  # # #  #     
 #   #  #   #   ###   ####   #   #   ###   #   #   ###                                                      
"""
print(red(intro))
print(black("========================================================"))

disclaimer = """
Created by CandyScriptz. Open source scanner tool.
This tool is to be used for educational
purposes only. Please do not use illegally for
malicious intent as that is not advised. For
any issues or reports contact the owner.
"""
print(black(disclaimer))
print("\033[31;40mSCANNER MENU\033[m")
print("\n")
print(yellow("[1]")+green(" Ping a target"))
print(yellow("[2]")+green(" Scan ports"))
print(yellow("[3]")+green(" Exit Program"))

userChoice = int(input(yellow("Enter an option: ")))
print("\n")

if (userChoice == 1):

    print(yellow("CTRL + C to stop ping"))
    print("\n")
    targetPing = input(yellow("Enter an address to ping: "))
    response = os.system("ping " + targetPing)
    os.system("date")

elif (userChoice == 2):
    
    targetScan = input(yellow("Enter an address to scan: "))
    ts_ip = gethostbyname(targetScan)
    print("Starting scan on ", ts_ip)
    for i in range(1,500):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((ts_ip, i))
        if (conn == 0):
            print("Port %d: OPEN" % (i,))
        s.close()
    print("Time taken:", time.time() - startTime)

elif (userChoice == 3):
    print(black("\nThanks for using!"))
    
else:
    print(red("Invalid choice. Exiting!"))
    exit()
