
import datetime

#Logged in message
def successfulLogin():
    # Login Success Message
    print("""
-----------------------------------------------------------------------------
[{}] Successfully Logged In To Main Discord Token!
-----------------------------------------------------------------------------
    """.format(datetime.datetime.now()))

#Shows all of the logged users
def successLoadingUsers(discordUserList):
    print("Discord Users:")
    for x in range (len(discordUserList)):
        print (f"[{datetime.datetime.now()}] Successfully Loaded [{discordUserList[x].name}] ")

    print ("\n")

def successGettingChannels(channelIDList):
    print("Channels:")
    if len(channelIDList) != 0:
        for x in range(len(channelIDList)):
            print(f"[{datetime.datetime.now()}][{channelIDList[x]}] Now Monitoring Channel")
        print("\n")
    else:
        print(f"[{datetime.datetime.now()}] Now Monitoring [All] Channels")
        print("\n")

def displayLoggs():
    print ("Logged Events: \n ")
    

def discordTokenError():
    print(f"[{datetime.datetime.now()}] Please Enter A List Of Discord User Name and Tokens In The Format As Mentioned In the ReadMe.md Then Restart This Program!")
    exit()