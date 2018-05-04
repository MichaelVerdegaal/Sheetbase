import discord
from discord.ext import commands

version = '1.3'
bot = commands.Bot(command_prefix="?", description="Sheetbase. A weird mashup between a discord bot, "
                                                   "google spreadsheets, and wannabe database.")
status_playing = "Christopher Columnbus"


@bot.event
async def on_ready():
    bot.load_extension('Sheetbase')
    bot.load_extension('Searching')
    bot.load_extension('Updating')
    print("Sheetbase online, version {}".format(version))
    print("Logged in as: {}||{}#{}".format(bot.user.id, bot.user.name, bot.user.discriminator))
    print("Status loaded as: |{}".format(status_playing))
    await bot.change_presence(activity=discord.Game(name=status_playing))


@bot.event
async def on_message(message):
    await bot.process_commands(message)


bot.run('NDQwODMzMjI0NjM0MDA3NTYy.DcyhnA.IgrD3bihTWQ-uUCURRNfZKzNDGU')
