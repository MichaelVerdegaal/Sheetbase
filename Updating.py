import discord
from discord.ext import commands
import Util as Util
import gspread


class Updating:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setCell(self, ctx, row, col, *,  content=""):
        """|Set the content of a specified cell"""
        gc = Util.Util.gc
        user_id = str(ctx.message.author.id)
        worksheet = gc.open(user_id).sheet1
        if row is None:
            await ctx.send('Please insert the coordinates correctly.')
        elif col is None:
            await ctx.send('Please provide a column value')
        else:
            worksheet.update_cell(row, col, content)
            if content:
                await ctx.send('Cell ({},{}) Updated to {}'.format(row, col, content))
            else:
                await ctx.send('Cell ({},{}) cleared.'.format(row, col))


def setup(bot):
    bot.add_cog(Updating(bot))
