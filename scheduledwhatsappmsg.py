import pywhatkit as pwk # pip install pywhatkit
# WhatsApp Web has to be Logged In

no = input("Enter the Number along with Country Code to send the Message to : ") # Example : +911234567890
msg = input("Enter the Message : ") # Example : Hi!

# Set delay for send
import datetime
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 1  # Sending 1 minute later

pwk.sendwhatmsg(no, msg, hour, minute)
