import discord
import random
from discord.ext import commands
from datetime import datetime
from datetime import date
import yaml
import asyncio

debug = False # to get more precise information in the log
botVersion = '1.2.1'
bot = commands.Bot(command_prefix=["!", "kiyu ", 'gros con '])


@bot.event
async def on_ready():  # print in the console when bot wake up
    print(f"[INFO] Bot initialized as excepted (botVersion = {botVersion})")
    await bot.change_presence(activity=discord.Game("regarde Beastars"))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("Cette commande n'existe pas <:grimacing:831844920330551338>")
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send(
            ("Tu n'as pas la permission de faire cette commande, "
            f"{ctx.author.mention}"))
    if isinstance(error, discord.ext.commands.errors.BadArgument):
        await ctx.send('Tu sais pas écrire une commande, haha!')
    else:
        print('Une erreur inconnue est survenue')



@bot.command(name="horaire")
async def timetable(ctx):
    await ctx.channel.send('ON à pas école gros con')


@bot.command(name="mails")
async def mails(ctx):
    RandomMail = random.randrange(1, 12)
    await ctx.send(file=discord.File(f"Assets/images/MailsDB/MailZeippen{RandomMail}.png"))
    if debug:
        print(f"[DEBUG] !mails : Image {RandomMail} printed in channel ID {ctx.channel.id}")
    await asyncio.sleep(5)
    await ctx.message.delete()


@bot.command(name="bamboula", aliases=["b"])
async def bamboula(ctx):
    await ctx.send("https://youtu.be/Agtyo-Rem3Q")
    if debug == True:
        print(f"[DEBUG] !bamboula in channel ID {ctx.channel.id}")
    await asyncio.sleep(5)
    await ctx.message.delete()


@bot.command(name="love", aliases=["l"])
async def love(ctx, Personne1, Personne2):
    if ctx.message.channel.id == 763352957579690018:
        botChannel = discord.utils.get(ctx.guild.channels, id=768194273970880533)
        messageBot = await ctx.send(
            (f"Va faire cette commande dans {botChannel.mention}"
            "ou je te soulève <:rage:831149184895811614>"))
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
        await ctx.send(f"Tu t'es pris pour qui ? {ctx.message.author.mention}")
        if debug:
            print("[DEBUG] !love : Someone tried to use a banned word !")
        return

    LoveRate = random.randrange(0, 100)
    await ctx.send(
        (f"L'amour entre **{Personne1}** et **{Personne2}**"
        f" est de **{LoveRate}%** <:flushed:830502924479758356>"))
    if debug:
        print(
            (f"[DEBUG] !love : The love rate ({LoveRate}%) between {Personne1}"
            f" and {Personne2} has been printed in channel ID {ctx.channel.id}"))


@bot.command(name="dumont", aliases=["tempmute", "fortnite", "michou", "brawlstars"])
async def dumont(ctx, userArgs: discord.Member = None):

    admin_role = discord.utils.get(ctx.guild.roles, name="*")
    mute_role = discord.utils.get(ctx.guild.roles, name="Mute")
    afk_channel = discord.utils.get(ctx.guild.channels, id=769125453314261002)

    authorizedMembers = {225282512438558720,357931867443560448,669992459060772864}
    user = ctx.message.author

    if userArgs != None:
        if user.id in authorizedMembers or admin_role in ctx.author.roles:
            user = userArgs
            await ctx.send(
                (f"{user.mention} vient de se faire envoyer en retenue par "
                "Mr Dumont pendant 3 minutes! <:angry:830881956870357023>"))
        else:
            await ctx.send(
                f"Tu t'es cru où ? {user.mention}, va en retenue! <:angry:830881956870357023>")
    else:
        await ctx.send(
            (f"{user.mention} vient de se faire envoyer en retenue par "
            "Mr Dumont pendant 3 minutes! <:angry:830881956870357023>"))

    await user.add_roles(mute_role)
    await ctx.message.delete()
    if user.voice != None:
        await user.move_to(afk_channel)
    await asyncio.sleep(180)
    await user.remove_roles(mute_role)


@bot.command(name="predict", aliases=["p"])
async def predict(ctx, args):
    if ctx.message.channel.id == 763352957579690018:
        bot_channel = discord.utils.get(ctx.guild.channels, id=768194273970880533)
        bot_message = await ctx.send(
            (f"Va faire cette commande dans {bot_channel.mention} "
            "ou je te soulève <:rage:831149184895811614>"))
        await asyncio.sleep(5)
        await ctx.message.delete()
        await bot_message.delete()
        return
    predictE = "Prédiction <:crystal_ball:830965316468867082> : "

    predictPhrases = [
        "Oui","Non", "Peut-Être <:thinking:830966162824888320>",
        ("Je ne devrais peut-être pas le dire"
        "<:face_with_hand_over_mouth:831149509287084052>"), "Sans aucun doute",
        "C'est probable", "Je ne pense pas", "Probablement pas",
        "Je ne suis pas sûr <:face_with_raised_eyebrow:831150009436995584>",
        "Il semblerait que oui", "Il semblerait que non...", 'Impossible',
        "La réponse pourrait vous choquer... ", 'ça c\'est sur à 100%', 'Faut pas rêver', 'C\'est ton destin',
        'Peu de chance', 'Et c\'est un non !', 'N\'y compte pas', 'Autant de chance qu\'une Isma sans échecs :)']
    await ctx.send(predictE + "**"+random.choice(predictPhrases)+"**")


@bot.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command(name="leave")
@commands.has_guild_permissions(ban_members=True)
async def leave(ctx):
    try:
        await ctx.voice_client.disconnect()
    except:
        await ctx.send(
            ("Tu n'as pas la permission d'exécuter cette commande,",
            f"{ctx.author.mention}"))


@bot.command(name='spam')
#@commands.has_guild_permissions(manage_messages=True)
async def spam(ctx, user: discord.User, num, *, message=None):
    if ctx.message.channel.id == 763352957579690018:
        bot_channel = discord.utils.get(ctx.guild.channels, id=768194273970880533)
        bot_message = await ctx.send(
            (f"Va faire cette commande dans {bot_channel.mention} "
            "ou je te soulève <:rage:831149184895811614>"))
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
        ctx.send("*J'ai réajusté la limite à 10, gros spammer*")
    if user in wordBanList:
        for x in range(num):
            await ctx.send(f'{ctx.message.mention.mention}')
        return
    if message == None:
        for x in range(num):
            await ctx.send(f'{user.mention}')
        return
    for x in range(num):
        await ctx.send(f'{user.mention} {message}')
    await ctx.message.delete()


@bot.command(name="insultes",
    aliases=["orraire", "horraire", "orairre", "horairre", "horzire", "orair",
             "oraire", "horair", "haraire", "horarie", "hroaire", "hraire",
             "hauraire", "haurair", "haurer"])
async def insultes(ctx):
    insultes = [
        "Apprend à écrire gros con", "**issou**", "Tu écris comme Prem",
        "Y'a de l'autisme dans l'air la non ?", "quelle orthographe dis donc",
        "Pire que Manon Boegen", "ew",
        "https://www.jaitoutcompris.com/rubriques/dictionnaire.php",
        "https://www.amazon.fr/Dictionnaire-Robert-Junior-illustré-CE-CM-6e/dp/2321015160/ref=sr_1_1",
        "Tu sais combien de temps ça ma pris pour coder tout ça ?"
        "moins que ça t'aurait pris pour corriger ce message",
        "Je te chie dessus depuis l'espace", "kinda cringe bro",
        "Mec tu me fais quoi là", "Apprend", "Hérétique!!!",
        "J'arrive te niquer prépare ton cul",
        "Tu sais même pas écrire une commande",
        "J'ai même plus envie de répondre",
        "Pourquoi t'es encore sur ce discord, on t'a toujours ban ?",
        "**soupir**","CHALLENGE:JE FERME MA GUEULE PENDANT 24HEURES!!! (ça tourne mal!!)",
        'Tu es le fils de Zeippen ou quoi ?', 'J\'appele l\'orphelinat']
    await ctx.send(random.choice(insultes))


@bot.command(name="github", aliases=["git"])
async def git(ctx):
    await ctx.send("https://github.com/Firminou/octo-timetable")
    if debug:
        print(f"[DEBUG] !github : repo sent")
    await asyncio.sleep(3)
    await ctx.message.delete()


@bot.command(name="réponse",aliases=["reponse", "raiponse"])
async def reponse(ctx, *,text):
    await ctx.send(text)
    await ctx.message.delete()

@bot.command(name="sarcasme",aliases=["majuscule", "maj", "sarcasm"])
async def sarcasm(ctx, *,sentence):
    new_sentence = ""
    number = 0  # Dummy number for tracking

    for letter in sentence.lower():
        if len(new_sentence) < 2:  # Creates the first two letter
            random_number = random.randint(0, 1)  # This randomly decides if the letter should be upper or lowercase
            if random_number == 0:
                new_sentence += letter.upper()
            else:
                new_sentence += letter
        else:
            if (new_sentence[number - 2].isupper() and new_sentence[number - 1].isupper() or new_sentence[
                number - 2].islower() and new_sentence[number - 1].islower()) == True:
                # Checks if the two letters before are both upper or lowercase
                if new_sentence[number - 1].isupper():  # Makes the next letter the opposite of the letter before
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

bot.run('')
