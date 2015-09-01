#The purpose of this program is to send a text message at a specific time.
#Copyright Brian Jopling 2015 top kek. Just kidding. I don't do copyrights.
#Use this however the heck you want to. I don't care.

"""
For the toAddress variable, follow the following format:

AT&T-                           phoneNumber@txt.att.net (SMS)
                                phoneNumber@mms.att.net (MMS)
T-Mobile-	                    phoneNumber@tmomail.net (SMS)
Verizon-	                    phoneNumber@vtext.com   (SMS)
                                phoneNumber@vzwpix.com  (MMS)
Virgin Mobile-        	        phoneNumber@vmobl.com   (SMS)

For this program, I'm using Gmail.
"""

import smtplib
import time
import sys

username = 'gmailUsername'
password = 'gmailPassword'
fromAddress = 'username@gmail.com'
toAddress = '5551234567@vtext.com' #See comment at the top. Change this to fit the address you want to send it to.
timeToSend = "15:30" #24-hour time.
msgContent = 'Hello friend.'
hasntSent = False #Not necessary for this example, but can be useful if you choose to modify this program.

def getTime():
    return time.strftime("%H:%M")

def textSend():
    server = smtplib.SMTP('smtp.gmail.com:587') #This is how you do it using Gmail. If you use another email service, you'll have to change this.
    server.starttls()
    server.login(username,password)
    server.sendmail(fromAddress, toAddress, msgContent)
    server.quit()

while True:
    if hasntSent == False:
        if getTime() == timeToSend:
            textSend()
            print "Sent at " + getTime() + "!"
            hasntSent = True
            sys.exit()
