import asyncio
import sys
import traceback
import datetime
import discord
from discord.ext import commands
from utils.congratulator import celebrate


description = '''Birthday-bot will remember the date your  friends don\'t, let's party!'''

modules = {'cogs.birthday', 'cogs.channels_management'}

bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Birthday-Bot starting...')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='with you at parties'))

    print('Loading cogs...')
    if __name__ == '__main__':
        modules_loaded = 0
        for module in modules:
            try:
                bot.load_extension(module)
                print('\t' + module)
                modules_loaded += 1
            except Exception as e:
                traceback.print_exc()
                print(f'Error loading the extension {module}', file=sys.stderr)
        print(str(modules_loaded) + '/' + str(modules.__len__()) + ' modules loaded')
        print('Systems 100%')
    print('------')

# Periodically celebrate
bot.loop.create_task(celebrate(bot))
# Test bot
bot.run('Mzc1NjQ1MDYwODk0NTU2MTYy.DNy2Qw.JQEl9nSWwdfqNwPcA3SgJnD41v4')
