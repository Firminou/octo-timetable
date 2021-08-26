import discord
import random
from discord.ext import commands
from datetime import datetime
from datetime import date
import asyncio

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Successfully loaded Moderation Cog')

    @commands.command(name='dumont', aliases=['tempmute', 'fortnite', 'michou', 'brawlstars'])
    async def dumont(self, ctx, userArgs: discord.Member = None):
        """A spinoff of the tempmute command, the command work on yourself as well as others (if you have the necessary permissions, if you don't have the permissions and try on someone else, you get tempmuted)

        Args:
            ctx (discord.ext.commands.Context): The "context" of the command (in this case, used to get the channel and the author of the command).
            userArgs (discord.Member, optional): The user that should be affected by the command. If None, the user that will be affected by the command will be the author of the command.
        """

        admin_role = discord.utils.get(ctx.guild.roles, name='*')
        mute_role = discord.utils.get(ctx.guild.roles, name='Mute')
        afk_channel = discord.utils.get(ctx.guild.channels, id=769125453314261002)

        authorizedMembers = {225282512438558720, 669992459060772864}
        user = ctx.message.author

        if userArgs != None:
            if user.id in authorizedMembers or admin_role in ctx.author.roles:
                user = userArgs
                await ctx.send(
                    (f'{user.mention} vient de se faire envoyer en retenue par ', 
                    'Mr Dumont pendant 3 minutes! <:angry:830881956870357023>'))
            else:
                await ctx.send(
                    f'Tu t\'es cru où ? {user.mention}, va en retenue! <:angry:830881956870357023>')
        else:
            await ctx.send(
                (f'{user.mention} vient de se faire envoyer en retenue par '
                'Mr Dumont pendant 3 minutes! <:angry:830881956870357023>'))

        await user.add_roles(mute_role)
        await ctx.message.delete()
        if user.voice != None:
            await user.move_to(afk_channel)
        await asyncio.sleep(180)
        await user.remove_roles(mute_role)

def setup(bot):
    bot.add_cog(Moderation(bot))