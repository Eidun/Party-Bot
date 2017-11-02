import discord
from discord.ext import commands

from utils.data import channels


class Channels:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_role('ADMIN')
    async def add_congratulate_channel(self, ctx, channel: discord.Channel):
        """<channel name>"""
        if channel.id not in channels:
            channels[channel.id] = channel
            await self.bot.send_message(ctx.message.channel, channel.name + ' added to congratulation channels.')

    @commands.command(pass_context=True)
    @commands.has_role('ADMIN')
    async def remove_congratulate_channel(self, ctx, channel: discord.Channel):
        """<channel name>"""
        if channel.id  in channels:
            del channels[channel.id]
            await self.bot.send_message(ctx.message.channel, channel.name + ' removed from congratulation channels.')

    @commands.command(pass_context=True)
    @commands.has_role('ADMIN')
    async def get_congratulate_channels(self, ctx):
        """Writes the list of  current channels"""
        output = 'There is a total of {} channels:'.format(len(channels))
        for channel in channels.values():
            output += '\n\t-' + channel.name
        await self.bot.send_message(ctx.message.channel, output)


def setup(bot):
    bot.add_cog(Channels(bot))
