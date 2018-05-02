import discord
from discord.ext import commands
import os

version = '1.1'
bot = commands.Bot(command_prefix="?", description="Sheetbase. A weird mashup between a discord bot, "
                                                   "google spreadsheets, and a database.")
status_playing = "Playing with tables"


@bot.event
async def on_ready():
    bot.load_extension('Sheetbase')
    bot.load_extension('Sheet')
    print("Sheetbase online, version {}".format(version))
    print("Logged in as: {}||{}#{}".format(bot.user.id, bot.user.name, bot.user.discriminator))
    print("Status loaded as: |{}".format(status_playing))
    await bot.change_presence(activity=discord.Game(name=status_playing))


@bot.event
async def on_message(message):
    await bot.process_commands(message)


bot.run('Token')
