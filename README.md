## Synopsis

This project was made to allow discord bots an easy way to persistently store data, but without having to dabble in databases, and database hosting. Google spreadsheets is a good solution since they allocate you 15GB of data for free in your Google drive, and the sheets themself are easy to understand.

## Dependecies 

Packages:
[Google api client](https://github.com/google/google-api-python-client)  
[Gspread] (https://github.com/burnash/gspread)  
[Discord.py Rewrite version] (https://github.com/Rapptz/discord.py/tree/rewrite)  

Other:
-Google account  
-[Google api client credentials] (https://gspread.readthedocs.io/en/latest/oauth2.html)  
-A discord bot account and it's [token] (https://discordpy.readthedocs.io/en/rewrite/discord.html)  

Place your token in main.py, in the bot.run('TOKEN HERE) line  
Place your client_credentials.json in your project directory  