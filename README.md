# 🤖MultiThreaded-Discord-Invite-Joiner
Automates joining discords servers, through discord self bot with Discord.py.

## 📣 Read First!
Self botting can result in your account getting banned!
If the program sends too many requests in a short time interval, it is very likely you could be banned!
Use this program only if you understand the risks involved!

The program reads through all messages, looking for any and all discord invites, once one is found, it will automatically attempt
to join the server through discord's APIs.

## ❓How to use the program:

**Setting up 'tokens.txt'**
The pre-existing example in the file is 'DiscordTagHere#0001:TokenHere' <-- Delete Afterwards
Place as many discord tags and tokens as you would like in the same format!

To Locate your discord token, visit the following video if your unsure how:
https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

Then replace the code in the main.py,
token = "Token" #Replace Token with the actual token of the discord account which will recieve the messages. Note: Only invites visable to this account will be joined.

**Setting up 'Channel ID.txt'**
If you don't want the bot to monitor every single channel in every single discord server, copy and paste select channel IDs you want the program to read from, line by line into the file.
