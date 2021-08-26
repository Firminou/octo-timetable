import discord
import random
from discord.ext import commands
from datetime import datetime
from datetime import date
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Successfully loaded Fun Cog')

    @commands.command(name='horaire')
    async def timetable(self, ctx):
        """the horaire command is currently deprecated, if we need it again, we'll rework the command and put it back in use
        """
        await ctx.channel.send('Ouvre Smartschool pour voir ton horaire connard')

    @commands.command(name='mails')
    async def mails(self, ctx):
        """A command that send randoms email sent from our school headmistress (we hate her)
        """
        RandomMail = random.randrange(1, 12)
        await ctx.send(file=discord.File(f'Assets/images/MailsDB/MailZeippen{RandomMail}.png'))
        await asyncio.sleep(5)
        await ctx.message.delete()

    @commands.command(name='bamboula', aliases=['b'])
    async def bamboula(self, ctx):
        """A command that send a link to a youtube video of our teacher telling "Who is Y'a du bamboula"
        
        Args : 
            ctx (discord.ext.commands.Context) : The "context" of the command (in this case, it is used to send the link in the proper channel)
        """
        await ctx.send('https://youtu.be/Agtyo-Rem3Q')
        await asyncio.sleep(5)
        await ctx.message.delete()
    
    @commands.command(name='predict', aliases=['p'])
    async def predict(self, ctx, args):
        """A "8-ball predictor", answer a random positive/neutral/negative phrase 

        Args:
            ctx (discord.ext.commands.Context): The "context" of the command (in this case, it is used to send the response in the proper channel)
            args (string): Used to have a mandatory argument and avoid to have user using !predict without anything to predict)
        """
        if ctx.message.channel.id == 848988652109561866:
            bot_channel = discord.utils.get(ctx.guild.channels, id=768194273970880533)
            bot_message = await ctx.send(
                (f'Va faire cette commande dans {bot_channel.mention} ',
                'ou je te soulève <:rage:831149184895811614>'))
            await asyncio.sleep(5)
            await ctx.message.delete()
            await bot_message.delete()
            return
        predictE = 'Prédiction <:crystal_ball:830965316468867082> : '

        predictPhrases = [
            'Oui', 'Non', 'Peut-Être <:thinking:830966162824888320>',
            ('Je ne devrais peut-être pas le dire'
            '<:face_with_hand_over_mouth:831149509287084052>'), 'Sans aucun doute',
            'C\'est probable', 'Je ne pense pas', 'Probablement pas',
            'Je ne suis pas sûr <:face_with_raised_eyebrow:831150009436995584>',
            'Il semblerait que oui', 'Il semblerait que non...', 'Impossible',
            'La réponse pourrait vous choquer... ', 'ça c\'est sur à 100%', 'Faut pas rêver', 'C\'est   ton destin',
            'Peu de chance', 'Et c\'est un non !', 'N\'y compte pas', 'Autant de chance qu\'une Isma    sans échecs :)']
        await ctx.send(predictE + '**'+random.choice(predictPhrases)+'**')
    
    @commands.command(name='love', aliases=['l'])
    async def love(self, ctx, Personne1, *, Personne2):
        """A "love test" command, if all arguments are fulfilled, return a phrase including a random percentage

        Args:
            ctx (discord.ext.commands.Context): The "context" of the command (in this case, it is used to answer in the right channel)
            Personne1 (string): First lover to be tested, also used to have a mandatory argument
            Personne2 (string): same as Personne1
        """
        if ctx.message.channel.id == 848988652109561866:
            botChannel = discord.utils.get(ctx.guild.channels, id=768194273970880533)
            messageBot = await ctx.send(
                (f'Va faire cette commande dans {botChannel.mention}',
                'ou je te soulève <:rage:831149184895811614>'))
            await asyncio.sleep(5)
            await ctx.message.delete()
            await messageBot.delete()
            return

        wordBanList = {'@everyone', '@here', '<@&763489250162507809>',
                       '<@&777564025432965121>','<@&822200827347075132>',
                       '<@&763815680306184242>','<@&764422266560839680<',
                       '<@&763815728972300338>','<@&763815728972300338>',
                       '<@&763815228323528725>','<@&763815784904261632>',
                       '<@&764422166116171806>','<@&764422057353936897>',
                       '<@&804807279043674143>','<@&828664814678179861>',
                       '<@&823562218095640646>','<@&823638574809219163>'}
        if Personne1 in wordBanList or Personne2 in wordBanList:
            await ctx.send(f'Tu t\'es pris pour qui ? {ctx.message.author.mention}')
            return
        LoveRate = random.randrange(0, 100)
        await ctx.send(
            (f'L\'amour entre **{Personne1}** et **{Personne2}**'
            f' est de **{LoveRate}%** <:flushed:830502924479758356>'))
        
    @commands.command(name='spam')
    #@commands.has_guild_permissions(manage_messages=True)
    async def spam(self, ctx, user: discord.User, num, *, message=None):
        """A command that... spam

        Args:
            ctx (discord.ext.commands.Context): The "context" of the command (used to spam in the channel where the command has been executed).
            user (discord.User): The user that shall be pinged
            num (int): the number of times to spam (to a maximum of 10)...
            message (string, optional): A message to spam. Defaults to None.
        """
        if ctx.message.channel.id == 848988652109561866:
            bot_channel = discord.utils.get(self.isma_guild.guild.channels, id=768194273970880533)
            bot_message = await ctx.send(
                (f'Va faire cette commande dans {bot_channel.mention} ',
                'ou je te soulève <:rage:831149184895811614>'))
            await asyncio.sleep(5)
            await ctx.message.delete()
            await bot_message.delete()
            return
        wordBanList = {'@everyone', '@here', '<@&763489250162507809>',
                       '<@&777564025432965121>','<@&822200827347075132>',
                       '<@&763815680306184242>','<@&764422266560839680<',
                       '<@&763815728972300338>','<@&763815728972300338>',
                       '<@&763815228323528725>','<@&763815784904261632>',
                       '<@&764422166116171806>','<@&764422057353936897>',
                       '<@&804807279043674143>','<@&828664814678179861>',
                       '<@&823562218095640646>','<@&823638574809219163>'}
        num = int(num)
        if num > 10:
            num = 10
            spam_message = await ctx.send('*J\'ai réajusté la limite à 10, gros spammer*')
            await spam_message.delete(delay=5)
        if user in wordBanList:
            for x in range(num):
                await ctx.send('Alors, non...')
            return
        if message == None:
            for x in range(num):
                await ctx.send(f'{user.mention}')
            return
        await ctx.message.delete()
        for x in range(num):
            await ctx.send(f'{user.mention} {message}')

    @commands.command(name='réponse', aliases=['reponse', 'raiponse'])
    async def reponse(self, ctx, * ,text):
        """A answer that repeats and then delete the message sent after 

        Args:
            ctx (discord.ext.commands.Context): The "context" of the command, used to
            text (string): the text to reply back
        """
        await ctx.send(text)
        await ctx.message.delete()

    @commands.command(name='sarcasme', aliases=['majuscule', 'maj', 'sarcasm'])
    async def sarcasm(self, ctx, *, sentence):
        """Same as sarcasm but set 

        Args:
            ctx (discord.ext.commands.Context): U should know right ?
            sentence (string): the phrase to repeat
        """
        new_sentence = ''
        number = 0  # Dummy number for tracking
        for letter in sentence.lower():
            if len(new_sentence) < 2:  # Creates the first two letter
                random_number = random.randint(0, 1)  # This randomly decides if the lettershould be       upper or lowercase
                if random_number == 0:
                    new_sentence += letter.upper()
                else:
                    new_sentence += letter
            else:
                if (new_sentence[number - 2].isupper() and new_sentence[number - 1].isupper()or        new_sentence[
                    number - 2].islower() and new_sentence[number - 1].islower()) == True:
                    # Checks if the two letters before are both upper or lowercase
                    if new_sentence[number - 1].isupper():  # Makes the next letter theopposite of         the letter before
                        new_sentence += letter.lower()
                    else:
                        new_sentence += letter.upper()
                else:
                    random_number = random.randint(0, 1)
                    if random_number == 0:
                        new_sentence += letter.upper()
                    else:
                        new_sentence += letter
            number += 1  # Add one more to the tracking
        await ctx.send(new_sentence)
        await ctx.message.delete()

    @commands.command(name='insultes',
        aliases=['orraire', 'horraire', 'orairre', 'horairre', 'horzire', 'orair',
                 'oraire', 'horair', 'haraire', 'horarie', 'hroaire', 'hraire',
                 'hauraire', 'haurair', 'haurer', ])
    async def insultes(self, ctx):
        """A command that send a random offense :p

        Args:
            ctx (discord.ext.commands.Context): The "context" of the command (used to send the insult in the right channel)
        """
        insultes = [
            'Apprend à écrire gros con', '**issou**', 'Tu écris comme Prem',
            'Y\'a de l\'autisme dans l\'air la non ?', 'quelle orthographe dis donc',
            'Pire que Manon Boegen', 'ew',
            'https://www.jaitoutcompris.com/rubriques/dictionnaire.php',
            'https://www.amazon.fr/Dictionnaire-Robert-Junior-illustré-CE-CM-6e/dp/2321015160/ref=sr_1_1',
            ('Tu sais combien de temps ça ma pris pour coder tout ça ? ',
            'moins que ça t\'aurait pris pour corriger ce message'),
            'Je te chie dessus depuis l\'espace', 'kinda cringe bro',
            'Mec tu me fais quoi là', 'Apprend', 'Hérétique!!!',
            'J\'arrive te niquer prépare ton cul',
            'Tu sais même pas écrire une commande',
            'J\'ai même plus envie de répondre',
            'Pourquoi t\'es encore sur ce discord, on t\'a toujours pas ban ?',
            '**soupir**','CHALLENGE: JE FERME MA GUEULE PENDANT 24HEURES!!! (ça tourne mal!!)',
            'Tu es le fils de Zeippen ou quoi ?', 'J\'appelle l\'orphelinat']
        await ctx.send(f'{ctx.author.mention}, {random.choice(insultes)}')

def setup(bot):
    bot.add_cog(Fun(bot))