import discord
from discord.ext import commands
import Util as Util
import gspread


class Sheetbase:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def ping(self, ctx):
        """|Used to test if bot is responsive and online"""
        await ctx.send("pong")

    @commands.command()
    async def start(self, ctx):
        """|Sets up a spreadsheet for your discord account."""
        gc = Util.Util.gc
        titles_list = []
        for worksheet in gc.openall():
            titles_list.append(worksheet.title)
        user = ctx.message.author
        user_id = str(user.id)
        if user_id not in titles_list:
            sh = gc.create(user_id)
            sh.share(value=Util.Util.share_email, perm_type='user', role='writer', notify=True,
                     email_message='A Sheetbase has been created:\n User {}\nDiscord ID {} '.format(user.name, user_id))
            await ctx.send(user.name + ", your Sheetbase has been created")
        else:
            await ctx.send('You already have a Sheetbase created. If you need extra workspace, '
                           'please create a new worksheet inside your Sheetbase')

    @commands.command()
    async def share(self, ctx, email):
        """Shares you Sheetbase with an user."""
        gc = Util.Util.gc
        user_id = str(ctx.message.author.id)
        user = ctx.message.author
        worksheet = gc.open(user_id).sheet1
        worksheet.share(value=email, perm_type='user', role='writer', notify=True,
                        email_message='An user has shared his Sheetbase with you!\nUser {}\nDiscord ID {} '.format(
                            user.name, user_id))
        await ctx.send("Sheetbase has been shared with this user")
        await ctx.message.delete()

    @commands.command()
    async def getSheets(self, ctx):
        """|Gets all sheets and their id's on the linked account"""
        gc = Util.Util.gc
        dc = {}
        for spreadsheet in gc.openall():
            dc[spreadsheet.title] = spreadsheet.id
        await ctx.send(dc)

    @commands.command(hidden=True)
    async def getPerms(self, ctx, sheet_id):
        """|Gets all permissions of a sheet"""
        gc = Util.Util.gc
        perms = gc.list_permissions(sheet_id)
        await ctx.send(perms)

    @commands.command()
    async def getId(self, ctx):
        """|Gets your sheet id"""
        gc = Util.Util.gc
        user_id = str(ctx.message.author.id)
        dc = {}
        for worksheet in gc.openall():
            dc[worksheet.title] = worksheet.id
        await ctx.send("Your spreadsheet ID is: " + dc[user_id])

    @commands.command()
    async def delete(self, ctx):
        """|Deletes your Sheetbase"""
        gc = Util.Util.gc
        user_id = str(ctx.message.author.id)
        dc = {}
        for worksheet in gc.openall():
            dc[worksheet.title] = worksheet.id
        gc.del_spreadsheet(dc[user_id])
        await ctx.send("Your sheetbase has been deleted.")

    @commands.command()
    async def deleteManual(self, ctx, sheet_id):
        """|For deleting a spreadsheet manually, in case problems occur (like duplicate sheets).
        Insert sheet id as parameter."""
        gc = Util.Util.gc
        gc.del_spreadsheet(sheet_id)
        await ctx.send('Sheet deleted')


def setup(bot):
    bot.add_cog(Sheetbase(bot))
