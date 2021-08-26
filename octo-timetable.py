import discord
import random
from discord.ext import commands
from datetime import datetime
from datetime import date
import asyncio
import os

botVersion = '1.2.2'
bot = commands.Bot(command_prefix=['!', 'kiyu ', 'gros con '])

@bot.event
async def on_ready():  # print in the console when bot wake up
    print(f'[INFO] Bot initialized as excepted (botVersion = {botVersion})')
    await bot.change_presence(activity=discord.Game('pleure de sa nouvelle classe'))

@bot.event
async def on_command_error(ctx, error):
    """This is the global error handler used when octo-timetable assume an exception

    Args:
        ctx (discord.ext.commands.Context): The "context" of the error (in this case, "ctx" is used to send the error message in the proper channel and/or ping the user that executed the command)
        error (discord.ext.commands.errors.[ErrorType]): The type of the error that occured
    """
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        return
    elif isinstance(error, (discord.ext.commands.UserInputError, discord.ext.commands.TooManyArguments, discord.ext.commands.errors.BadArgument)):
        await ctx.send('t tellement nul que t\'arrive pas à écrire une commande lol')
    elif isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send(f'Tu n\'as pas la permission de faire cette commande, {ctx.author.mention}')
    elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
        await ctx.send(f'Il semblerait que je n\'ai pas la\les permission(s) d\'exécuter cette commande <:sweat:880156413509394452> (permissions manquantes : {error.missing_perms})')
    else:
        await ctx.send(f'Oh oh, une erreur inconnue que le dresseur de Kiyu n\'a pas prévu vient de survenir <:sweat:880156413509394452> (erreur : {error})')

for filename in os.listdir('.'):
    if filename.endswith('.py') and \
    filename.startswith('cog_'):
        bot.load_extension(f'{filename[:-3]}')

@bot.command(name='github', aliases=['git'])
async def git(ctx):
    await ctx.send('https://github.com/Firminou/octo-timetable')
    await asyncio.sleep(3)
    await ctx.message.delete()

@bot.command(name='status')
@commands.has_guild_permissions(ban_members=True)
async def status(ctx, *, status):
    """Changes the status of the bot based on the user input

    Args:
        ctx (discord.ext.commands.Context)
        status (string): the new status
    """
    await bot.change_presence(activity=discord.Game(f'{status}'))
    message = await ctx.send(f'<:white_check_mark:880391887389859870> Ok, mon nouveau status est "{status}"')
    await message.delete(delay=5)
    await ctx.message.delete(delay=5)


bot.run('ODM4MTIyNTkyMzM3Nzg5MDE5.YI2gfQ.3SIeeaOy-FWysNv_wCeCj1cIoTM')
