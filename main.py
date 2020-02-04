import datetime
import discord
import requests
import threading 
import concurrent.futures
from userPrompts import *

token = "token" #Main Account To Read Messages Off From
client = discord.Client()

#Defines class for discordAccounts
class discordUser:
    def __init__(self,discordName,token):
        self.name = discordName
        self.token = token
        
#Creates a object for each discord acount
def storedUsers():
    discordUserList = []
    with open ("tokens.txt", "r") as file:
        for line in file:
            line = line.strip()
            info = line.split(":")
            discordUserList.append(discordUser(info[0],info[1]))
    return discordUserList


#Reads all of the channel IDs into a List
def storedChannelIDs():
    idList = []
    with open ("channel ID.txt", "r") as file:
        for id in file:
            idList.append(int(id.strip()))
    return idList


#Reading From Files
discordUserList = storedUsers()
channelIDList = storedChannelIDs()

if (len(discordUserList) == 0):
    discordTokenError()
    
#Prompt
successfulLogin()
successLoadingUsers(discordUserList)
successGettingChannels(channelIDList)
displayLoggs()

