import os
import discord
from discord.ext import commands
import aiohttp
from io import BytesIO
from discord.utils import get
import asyncio
import logging
import datetime, time

client = commands.AutoShardedBot(commands.when_mentioned_or('!'))


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def c(ctx, msg: str):
    try:
        if ctx.channel == client.get_channel(828261315692593172):

            mbed = discord.Embed(
                title='New Confession',
                description='Your message has been recorded and will be posted in #confessions anonymously. Moderators have the right to delete messages that are blah blah')

            demand = await ctx.send(embed=mbed)
            await ctx.message.delete()

            # send confession
            channel = client.get_channel(828478580254048278)  # confession channel
            mbed_confess = discord.Embed(
                title='Anonymous',
                description=msg
            )
            await channel.send(embed=mbed_confess)

            # log
            log = client.get_channel(828490996995719198)  # logs channel
            mbed_log = discord.Embed(
                title=f'New Confession from user id: {ctx.author.id}',
                description=f'Author Name: {ctx.author.name}'
            )

            mbed_log.set_footer(text=datetime.datetime.today())
            await log.send(embed=mbed_log)

        else:
            await ctx.send('Please use the proper channel')
    except:
        await ctx.message.delete()


@client.command()
async def commands(ctx):
    mbed = discord.Embed(
        title='Commands',
        description='!c to confess \n !commands for command list'
    )
    await ctx.send(embed=mbed)


client.run('ODI4NDY0NDc2Nzc2NTYyNzM5.YGp9qw.onVoLaiNYAEc-hCqvDlaycY0API')