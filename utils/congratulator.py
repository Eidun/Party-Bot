import asyncio
import discord
from utils.data import birthdays, channels, images, messages
from discord.ext import commands
import random
import datetime


async def celebrate(bot:commands.Bot):
    while not bot.is_closed:
        await asyncio.sleep(60 * 60 * 24)
        print(birthdays)
        birthday_people = get_birthday_people()
        for birth_person in birthday_people:
            user = birth_person[0]
            embed = discord.Embed(title='HAPPY {} BIRTHDAY, {}!!'
                                        .format(get_age(birth_person[1].year), user.display_name),
                                  description='This is your very special day',
                                  color=0xEE82EE)
            embed.set_author(name=user.display_name, icon_url=user.avatar_url)
            embed.add_field(name='Congratulations!', value=random.choice(messages))
            embed.set_image(url=random.choice(images))
            for channel in channels.values():
                await bot.send_message(channel, embed=embed)


def get_birthday_people():
    birthday_people = []
    for user in birthdays.values():
        birth_date = user[1]
        today = datetime.datetime.now()
        if today.day == birth_date.day and today.month == birth_date.month:
            birthday_people.append(user)
    return birthday_people


def get_age(year):
    today = datetime.datetime.now().year
    return today - year
