------------------------------
#############################################################
# PUT TOGETHER BY DWALF - 02OCT2021
# WARNING NOTE: THIS IS NOT A PLUGIN - DO NOT USE IT AS A OCTOPRINT PLUGIN
#
# NAME OCTOKITTY_LCD I2C 16x2 LCD DISPLAY - (README)
# VERSION 1.3 - NOT FOR COMMERCAIL USE - PERSONAL USE ONLY
# WITHOUT WARRNETY OR SUPPORT
# USE AT OWN RISK AND LIABILITY
#
# THANKS EVERYONE - ONLY ONE HOTEND tool0 SUPPORTED
# WORKS WITH OCTOPRINT 1.6 (0.18.0 Octoprint) and PY3
# TIP ME AT https://www.thingiverse.com/dwalf/designs
#
# REQUIRED ALL FILES IN '/home/pi' FOLDER
# THIS FILE '/home/pi/octokittylcd' RUN FROM 'sudo nano /etc/rc.local' AND MAKE EXECUTABLE 'CHMOD +x /home/pi/octokittylcd
# Or better 'sudo crontab -u pi -e'  add line at bottom '@reboot sudo /home/pi/octokittylcd'
# LCD DRIVER FILE 'I2C_LCD_driver.py'
# LCD DISPLAY FILE 'octolcd16x2.py'
# SEE README FILE
#
# RESOURCES
# https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
# https://community.octoprint.org/t/is-there-a-reliable-way-to-determine-if-a-print-job-is-in-pr$
# https://docs.octoprint.org/en/master/api/job.html#retrieve-information-about-the-current-job
#############################################################
------------------------------
DOWNLOAD AND INSTALL OCTOPI
------------------------------
https://octoprint.org/download/
Download Octoprint (https://unofficialpi.org/Distros/OctoPi/)
0.18.0 Octoprint

------------------------------
DOWNLOAD AND BALENAEtcher and IMAGE OCTOPI to SDCARD
------------------------------
https://www.balena.io/etcher/

------------------------------
UNplug SDCARD and put back in again (WIFI) 
------------------------------
open drive D:
Find and Edit file octopi-wpa-supplicant.txt in notepad

############################
## WPA/WPA2 secured
network={
  ssid="YOURWIFISSID"
  psk="YOURWIFIPASSWORD"
}
############################

------------------------------
Wire up the I2C LCD EXAMPLE
------------------------------
https://www.youtube.com/watch?v=3XLjVChVgec

only 4 wires

------------------------------
Insert you SDcard in your pi and boot it (switch on)
------------------------------

------------------------------
Setup Octoprint on the webpage 
------------------------------
Find the IP address in your router DHCP CLIENT LEASES look for "octopi" PC
If you cant find it look in windows 10 under NETWORK

Raspberry pi zero Disable ALL Webcam settings, wont work for a zero
Enable Virtual Printer for testing
Update if prompted

IN OCTOPRINT SETTINGS FIND 'API'
WRITE DOWN THE API KEY WE WILL NEED THIS 

------------------------------
SSH INTO YOUR PI WITH IP ADDRESS
------------------------------
Download Putty
https://www.chiark.greenend.org.uk/~sgtatham/putty/

Username = pi
Password = raspberry

Enable I2C in Raspi-Config

cmd = sudo raspi-config

3 INterface options -> P5 I2C - YES - OK - FINISH

cmd = sudo reboot

------------------------------
INSTALL THE FOLLOWING TO GET THE DISPLAY TO WORK
------------------------------
sudo apt-get install i2c-tools
sudo apt-get install python-smbus
sudo apt install -y jq

------------------------------
THESE TWO ARE NOT NEEDED IGNORE FOR NOW - ONLY INSTALL IF YOU HAVE ISSUES
------------------------------
sudo apt-get install python3-setuptools
sudo apt-get install python3-pip

------------------------------
REBOOT
------------------------------
sudo reboot

------------------------------
SSH LOGIN AGAIN
------------------------------
Check I2C address, should be 0x27 

cmd = i2cdetect -y 1

see end of this file if your address is diffrent

------------------------------
DOWNLOAD OctoKitty_LCD and unzip it in the /home/pi folder
------------------------------
You should have 3 files
octokittylcd
I2C_LCD_driver.py
octolcd16x2.py

make the octokittylcd executable

cmd = sudo chmod +x octokittylcd

--------------------------------
SET STARTUP FILE WHEN BOOT
--------------------------------
Enter the command and then edit the last line before the 'exit 0'
cmd = sudo nano /etc/rc.local  

#######################
/home/pi/octokittylcd
#######################

--------------------------------
ENTER THE API KEY IN octokittylcd
--------------------------------

cmd = sudo nano octokittylcd

Find the lines as below and enter your API KEY
#####################################
# OCTOPRINT API KEY
# ENTER YOUR KEY FROM OCTOPRINT HERE
#####################################
apikey='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # <-----------------------------ENTER YOUR API HERE--$

--------------------------------

YOU WILL SEE ALLOT OF SETTINGS CAN BE CHANGED WHERE YOU SEE <-------------------------------
THERE IS A BUILT IN SCREEN SAVER WHAT ONLY COMES ON WHEN READY
THERE IS ALSO A INFO SCREEN WHAT POPS UP DURING PRINTING WITH OTHER INFO
NOTE I PUT THIS ALL TOGETHER OVER 4 DAYS AND I DONT REALLY CODE AND I DONT REALLY KNOW PYTHON
HOW WE GOT HERE, WHO KNOWS LOL
I MIGHT DO A VERSION 2 WITH BUTTONS

--------------------------------
REBOOT WHEN ALL DONE
cmd = sudo reboot
SHOULD BE WORKING????
--------------------------------


PS this is not just for Pi Zero
if you have an older version of raspberry pi you may need to set a setting in I2C_LCD_driver.py 
Most PI wont need any changes done in this file. 
This is also where the LCD address is stored. If your Display has another address or not original PI 
then make changes here

###########################################################
# i2c bus (0 -- original Pi, 1 -- Rev 2 Pi) <---------------------------------------------
I2CBUS = 0

# LCD Address       
ADDRESS = 0x27 
###########################################################

ENJOY 
DWALF