import datetime
import discord
import requests
import threading 
import asyncio
import concurrent.futures
from userPrompts import *

token = "Token" #Main Account To Read Messages Off From
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

def attemptJoin(inviteCode,discordUser):
    URL = "https://discordapp.com/api/v6/invites/" + inviteCode
    headers = {
        "authorization": "{}".format(discordUser.token),
    }
    requestResponse = requests.post(url=URL, data="", headers=headers)
    
    print(f"[{datetime.datetime.now()}] [{discordUser.name}] Attempted to Join Discord")
    
    if requestResponse.status_code == 200:
        return(f"[{datetime.datetime.now()}] [{discordUser.name}]Successfully Attempted To Join Discord Invite")
    else:
        return(f"[{datetime.datetime.now()}] [{discordUser.name}]Failed To Join Discord Invite")
    
    
    
    
@client.event
async def on_message(message):
    if message.channel.id in channelIDList:
        if "discord.gg/" in message.content:
            print("[{}]".format(datetime.datetime.now()), "[Server: {0.guild.name}][#{0.channel}][{0.author}]:'{0.content}'".format(message))
            print("[{}] Found Invite".format(datetime.datetime.now()))
            indexNum = message.content.find("discord.gg/")
            indexNum += 11
            inviteCode = ""
            for x in range (indexNum,len(message.content)):
                if not (message.content[x] == " "):
                    inviteCode += message.content[x]
                else:
                    break
            print("[{}] Invite Code:".format(datetime.datetime.now()), inviteCode)
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = [executor.submit(attemptJoin,inviteCode,discordUser) for discordUser in discordUserList]

            for x in concurrent.futures.as_completed(results):
                print(x.result())
                
client.run(token, bot=False)
