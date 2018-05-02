import discord
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials
import Util as Util
import gspread
import os


class Sheet:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getRow(self, ctx, row):
        """|Retrieve all the data of a specified row"""
        gc = Util.Util.gc
        user_id = str(ctx.message.author.id)
        spreadsheet = gc.open(user_id).sheet1
        values_list = spreadsheet.row_values(row)
        if values_list:
            await ctx.send(values_list)
        else:
            await ctx.send("Row is empty")


def setup(bot):
    bot.add_cog(Sheet(bot))
