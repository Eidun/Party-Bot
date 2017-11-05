import datetime
import discord
from utils.data import messages
from discord.ext import commands

from utils.data import birthdays


class Happy:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_role('ADMIN')
    async def add_congratulate_message(self, ctx, message: str):
        """<new message>"""
        messages.append(message)
        await self.bot.send_message(ctx.message.channel, 'Message added.')

    @commands.command(pass_context=True)
    @commands.has_role('ADMIN')
    async def remove_congratulate_messages(self, ctx):
        """Removes ALL current messages"""
        messages = []
        await self.bot.send_message(ctx.message.channel, 'All messages removed.')


def setup(bot):
    bot.add_cog(Happy(bot))
