import datetime

from discord.ext import commands

from utils.data import birthdays


class Birthday:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def birthday(self, ctx, birthday_string=None):
        """<dd-mm-yyyy> None for know the current value"""
        # Get the author
        user = ctx.message.author

        if birthday_string is not None:
            birth_date = datetime.datetime.strptime(birthday_string, '%d-%m-%Y')
            birthdays[user.id] = [user, birth_date]
        if user.id in birthdays:
            birth_date = birthdays[user.id][1]
            await self.bot.say('Your birthday is {}'.format(birth_date.strftime('%d-%m-%Y')))
        else:
            await self.bot.say('Hey, I don\'t know your birthday yet!Try this command again with a valid date'
                               ' so I can remember it forever!')


def setup(bot):
    bot.add_cog(Birthday(bot))
