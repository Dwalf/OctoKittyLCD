#!/usr/bin/python3
#############################################################
# PUT TOGETHER BY DWALF - 01OCT2021
# WARNING NOTE: THIS IS NOT A PLUGIN - DO NOT USE IT AS A OCTOPRINT PLUGIN
#
# NAME OCTOKITTY_LCD I2C 16x2 LCD DISPLAY
# VERSION 1.1 - NOT FOR COMMERCAIL USE - PERSONAL USE ONLY
# WITHOUT WARRNETY OR SUPPORT
# USE AT OWN RISK AND LIABILITY
#
# THANKS EVERYONE
# WORKS WITH OCTOPRINT 1.6 and PY3
# TIP ME AT https://www.thingiverse.com/dwalf/designs
#
# RESOURSES
# https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
#############################################################

#########################
# IMPORT STATMENTS
# UNCOMMENT TO USE OTHER
#########################
import I2C_LCD_driver
#import socket
#import fcntl
#import struct
#import requests
#import json
#import commands
#import re
#import subprocess
import sys
#import os
#import shlex
from time import *

##############################
# OCTOPRINT API KEY ONLY FOR DEMO - DO NOT USE OR NEED
# ENTER YOUR KEY FROM OCTOPRINT HERE
##############################
#apikey = 'xxxxxxxxxxxxxxxxxxxxxxxx'

#########################
# CALL DRIVER FILE
#########################
mylcd = I2C_LCD_driver.lcd()

####################################
# DEMO GET PRINT JSON OR SEND COMMMANDS
# https://docs.octoprint.org/en/master/api/printer.html#retrieve-the-current-printer-state
# https://community.octoprint.org/t/how-interrogate-print-status-from-command-line/810/2
####################################
#commandocto = '/home/pi/oprint/bin/octoprint client -a ' + apikey + ' -h 127.0.0.1 get /api/connection'
#print(commandocto)
#json_s = commands.getstatusoutput(commandocto)
#print(json_s)
#json_p = json.dumps(json_s)
#print(json_p)

################################
# DEMO READ THE OCTOPRINT-CLI OUTPUT
# https://github.com/UserBlackBox/octoprint-cli#configuration
################################
# cliout = commands.getstatusoutput('/home/pi/.local/bin/octoprint-cli print status')

#################################
# PRINT TO THE SCREEN THE STATUS
# WE FIRST CLEAR THE SCREEN
# THE VAR ARE SENT FROM A BASH SCRIPT
#################################
mylcd.lcd_clear()
statval1='1'
statval2='2'
statval3='3'
statval4='4'
statval5='5'
statval6='6'
statval7='7'
statval8='8'
statval9='9'
lcdstat=sys.argv[1]

# VARIBLES SENT FROM BASH SCRIPT FOR DEBUGING
#print sys.argv[0]
#print sys.argv[1]
#print sys.argv[2]
#print sys.argv[3]
#print sys.argv[4]
#print sys.argv[5]

# BASIC INFO SCREEN
if lcdstat == statval1:
    mylcd.lcd_display_string(sys.argv[2], 1) #TOP SCREEN
    mylcd.lcd_display_string(sys.argv[3], 2) #BOTTOM SCREEN

# CHECK PRINTER CONNECTED OK SCREEN AND JSON AND API
if lcdstat == statval2:
    mylcd.lcd_display_string(sys.argv[2], 1) #TOP SCREEN
    mylcd.lcd_display_string(sys.argv[3], 2) #BOTTOM SCREEN
    #Turn the backlight off:
    mylcd.backlight(0)
    sleep(1)
    #Turn the Backlight on:
    mylcd.backlight(1)
    sleep(1)

# CLEAR THE SCREEN
if lcdstat == statval3:
    mylcd.lcd_clear()

# PRINTER STATUS SCREEN
if lcdstat == statval4:
    mylcd.lcd_display_string(sys.argv[2], 1, 0) #TOP SCREEN
    mylcd.lcd_display_string(sys.argv[3], 1, 10) #TOP SCREEN
    mylcd.lcd_display_string(sys.argv[4], 2, 0) #BOTTOM SCREEN
    mylcd.lcd_display_string(sys.argv[5], 2, 9) #BOTTOM SCREEN

# PRINTER ALARM SCREEN AND FLASH LED ON OFF
if lcdstat == statval5:
    mylcd.lcd_display_string(sys.argv[2], 1, 0) #TOP SCREEN
    mylcd.lcd_display_string(sys.argv[3], 1, 10) #TOP SCREEN
    mylcd.lcd_display_string(sys.argv[4], 2, 0) #BOTTOM SCREEN
    mylcd.lcd_display_string(sys.argv[5], 2, 9) #BOTTOM SCREEN
    #Turn the backlight off:
    mylcd.backlight(0)
    sleep(1)
    #Turn the Backlight on:
    mylcd.backlight(1)
    sleep(1)

# PRINTER SPECIAL SCREEN (MEOW)
if lcdstat == statval6:
    mylcd.lcd_display_string(sys.argv[2], 1, 4) #TOP SCREEN
    mylcd.lcd_display_string(sys.argv[3], 1, 11) #TOP SCREEN
    mylcd.lcd_display_string(sys.argv[4], 2, 5) #BOTTOM SCREEN

# PRINTER SCREEN OFF
if lcdstat == statval7:
    mylcd.lcd_display_string("SCREENSAVER", 1, 3) #TOP SCREEN
    mylcd.lcd_display_string("***********", 2, 3) #BOTTOM SCREEN
    #Turn the backlight off:
    mylcd.backlight(0)

# PRINTER BUTTON MESSAGES
if lcdstat == statval8:
    mylcd.lcd_display_string("*SHUTTING_DOWN*", 1, 3) #TOP SCREEN
    mylcd.lcd_display_string("****SERVER*****", 2, 3) #BOTTOM SCREEN
    #Turn the backlight off:
    mylcd.backlight(0)

# SCREEN SCROLL RIGHT TOO LEFT LONG
if lcdstat == statval9:
    mylcd.lcd_display_string(sys.argv[2], 1) #TOP SCREEN
    str_pad = " " * 16
    my_long_string = str_pad + sys.argv[3]
    for i in range (0, len(my_long_string)):
        lcd_text = my_long_string[i:(i+16)]
        mylcd.lcd_display_string(lcd_text,2) #BOTTOM SCREEN
        sleep(0.1)
        mylcd.lcd_display_string(str_pad,2)  #BOTTOM SCREEN
        sleep(0.1)

###############################
# FINISHED THE END OF FILE
###############################
