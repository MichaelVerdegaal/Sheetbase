import discord
from discord.ext import commands
import Util as Util
import gspread


class Searching:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def getCell(self, ctx, row, col):
        """|Retrieve the data of a specified cell"""
        gc = Util.Util.gc
        user_id = str(ctx.message.author.id)
        worksheet = gc.open(user_id).sheet1
        if row is None:
            await ctx.send('Please insert the coordinates correctly.')
        elif col is None:
            await ctx.send('Please provide a column value')
        else:
            val = worksheet.cell(row, col).value
            if val:
                await ctx.send(val)
            else:
                await ctx.send("Cell is empty")

    @commands.command()
    async def getRow(self, ctx, row):
        """|Retrieve all the data of a specified row"""
        gc = Util.Util.gc
        user_id = str(ctx.message.author.id)
        worksheet = gc.open(user_id).sheet1
        values_list = worksheet.row_values(row)
        if values_list:
            await ctx.send(values_list)
        else:
            await ctx.send("Row is empty")

    @commands.command()
    async def getCol(self, ctx, col):
        """|Retrieve all the data of a specified column"""
        gc = Util.Util.gc
        user_id = str(ctx.message.author.id)
        worksheet = gc.open(user_id).sheet1
        values_list = worksheet.col_values(col)
        if values_list:
            await ctx.send(values_list)
        else:
            await ctx.send("Column is empty")

    @commands.command()
    async def findCell(self, ctx, query):
        """|Tries to find a cell, with the specified content."""
        gc = Util.Util.gc
        user_id = str(ctx.message.author.id)
        worksheet = gc.open(user_id).sheet1
        try:
            cell = worksheet.find(query)
            await ctx.send("Found something at ({},{})".format(cell.row, cell.col))
        except gspread.exceptions.CellNotFound:
            await ctx.send("Nothing like that found.")


def setup(bot):
    bot.add_cog(Searching(bot))
