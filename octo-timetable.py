import discord
import random
from discord.ext import commands
from datetime import datetime
from datetime import date
import yaml
import asyncio

debug = False # to get more precise information in the log

botVersion = "1.2.0"

bot = commands.Bot(command_prefix=["!", "kiyu "])

monClass1 = ["Géographie", "Math", "Sciences", "Anglais", "Français", "Religion", "Anglais", "Math"]
tueClass1 = ["Histoire", "Religion", "Option (je sais pas mec)", "Math", "Math", "Langue 2", "Informatique/Étude",
             "Informatique/Étude"]
wedClass1 = ["Math", "Français", "Français", "Option (je sais pas mec)", "Langue 1", "/", "/", "/"]
thuClass1 = ["Histoire", "Sciences", "Français", "Langue 2", "Sport", "Langue 1", "Informatique/Étude",
             "Informatique/Étude"]
friClass1 = ["Étude", "Géographie", "Sciences", "Français", "Langue 1", "Sport", "Allemand/Étude", "Allemand/Étude"]
theClass1 = [monClass1, tueClass1, wedClass1, thuClass1, friClass1, monClass1, monClass1]

monClass2 = ["Latin/Étude", "Sport intensif", "Sport intensif", "Anglais", "Sciences", "Latin/Étude", "Religion",
             "Géographie/Anglais"]
tueClass2 = ["Math", "Histoire/Anglais", "Math", "Sciences", "Anglais/Histoire", "Allemand/Étude", "Français", "Français"]
wedClass2 = ["Sciences", "Math", "Anglais/Histoire", "Latin/Étude", "Anglais/Géographie", "/", "/", "/"]
thuClass2 = ["Math", "Histoire/Anglais", "Géographie/Anglais", "Allemand/Étude", "Français", "Français", "Math", "Étude"]
friClass2 = ["Labo", "Labo", "Français", "Anglais", "Latin/Étude", "Religion", "Allemand/Étude", "Allemand/Étude"]
theClass2 = [monClass2, tueClass2, wedClass2, thuClass2, friClass2, monClass2, monClass2]

monClass3 = ["Latin/Étude", "Math", "Math", "Géographie", "Étude", "Latin/Étude", "Sciences", "Anglais"]
tueClass3 = ["Math", "Anglais", "Français", "Religion", "Histoire", "Allemand/Étude", "Sport/Info", "Sport/Info"]
wedClass3 = ["Religion", "Français", "Histoire", "Latin/Étude", "Géographie", "/", "/", "/"]
thuClass3 = ["Math", "Anglais", "Anglais", "Allemand/Étude", "Faire des squats", "Français", "Science", "Français"]
friClass3 = ["Sciences", "Français", "Math", "Anglais", "Latin/Étude", "Faire des pompes", "Allemand/Étude",
             "Allemand/Étude"]
theClass3 = [monClass3, tueClass3, wedClass3, thuClass3, friClass3, monClass3, monClass3]

monClass4 = ["Math", "**Faire la saucisse**", "**Faire des roulades à la zelda", "Géographie", "Religion", "Sciences",
             "Sciences", "Anglais"]
tueClass4 = ["Français", "Anglais", "Sciences", "Français", "Histoire", "Allemand/Étude", "Étude", "Étude"]
wedClass4 = ["Français", "Math", "Histoire", "Sciences", "Géographie", "/", "/", "/"]
thuClass4 = ["Étude", "Anglais", "Anglais", "Allemand/Étude", "Religion", "Math", "Informatique/Étude",
             "Informatique/Étude"]
friClass4 = ["Français", "Math", "Math", "Anglais", "Sciences", "Français", "Allemand/Étude", "Allemand/Étude"]
theClass4 = [monClass4, tueClass4, wedClass4, thuClass4, friClass4, monClass4, monClass4]

monClass5 = ["Religion", "Histoire", "Français", "Français", "Math", "Sciences", "Sciences", "Étude"]
tueClass5 = ["Histoire", "Anglais", "Sciences", "**Faire des abdos**", "**Muscler son boule**", "Allemand/Étude", "Étude",
             "Étude"]
wedClass5 = ["Anglais", "Math", "Math", "Sciences", "Français", "/", "/", "/"]
thuClass5 = ["Géographie", "Français", "Anglais", "Allemand/Étude", "Religion", "Math", "Informatique", "Informatique"]
friClass5 = ["Anglais", "Anglais", "Math", "Géographie", "Sciences", "Français", "Allemand/Étude", "Allemand/Étude"]
theClass5 = [monClass5, tueClass5, wedClass5, thuClass5, friClass5, monClass5, monClass5]

monClass6 = ["Étude", "Comms", "Comms", "**Sport**", "Soulever des ~~bites~~ poids", "Anglais", "Math", "Math"]
tueClass6 = ["Science", "AHV", "Rel", "\"**Sport**\"", "\"**Sport**\"", "Sciences", "Histoire-Géo", "Flute"]
wedClass6 = ["IVP", "EVS", "EVS", "Anglais", "Étude", "/", "/", "/"]
thuClass6 = ["AHV", "Français", "Français", "**Kazoo**", "Religion", "Math", "Anglais", "Histoire-Géo"]
friClass6 = ["AHV", "IVP", "IVP", "Math", "Français", "Français", "Anglais", "Étude"]
theClass6 = [monClass6, tueClass6, wedClass6, thuClass6, friClass6, monClass6, monClass6]

schoolTimetableArray = [theClass1, theClass2, theClass3, theClass4, theClass5, theClass6]

jour_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"
                "dimanche"]  # I define each day of the week


@bot.event
async def on_ready():  # print in the console when bot wake up
    print(f"[INFO] Bot initialized as excepted (botVersion = {botVersion})")
    await bot.change_presence(activity=discord.Game("Affronte les arabes"))


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


def pourcentage(mode):
    nowPreciseDate = datetime.now()  # get exact date with seconds
    toPourcent = (int(nowPreciseDate.strftime("%H"))) * 60 + \
        int(nowPreciseDate.strftime("%M"))
    if mode == 0:
        if toPourcent <= 480:
            return 0
        elif 480 > toPourcent or toPourcent < 955:
            toPourcent = (toPourcent - 480) / 475 * 100
            return round(toPourcent, 1)
        else:
            return 100
    elif mode == 1:
        return round((((int(nowPreciseDate.strftime("%H"))) * 60) +
            (int(nowPreciseDate.strftime("%M")))) / 1440 * 100, 1)


def sendHoraire(ctx, minute, hour, currentDay): # TODO REWRITE sendHoraire
    schoolRole = 0  # need to be referenced before assignement
    classesFromConfig = yaml.load(open("config.yaml"), Loader=yaml.FullLoader).get("classes")
    role_class1, role_class2, role_class3, role_class4, role_class5, role_class6 = "","","","","",""
    schoolRoleArray = [role_class1, role_class2, role_class3, role_class4, role_class5, role_class6]
    hourList = yaml.load(open("config.yaml"), Loader=yaml.FullLoader).get("hours")
    minuteList = yaml.load(open("config.yaml"), Loader=yaml.FullLoader).get("minutes")
    for y in range(len(classesFromConfig)):
        schoolRoleArray[y] = discord.utils.get(ctx.guild.roles, name=classesFromConfig[y])
    for ima in range(len(classesFromConfig)):
        if schoolRoleArray[ima] in ctx.author.roles:
            schoolRole = ima

    period = -1
    if currentDay > 4:
        period = 0
        currentDay = 0
    elif hour >= hourList[9]+1 or hour == hourList[9] and minute > minuteList[9]:
        period = 0
        currentDay += 1
    elif hour < hourList[0]:
        period = 0
    else:
        incHour = 0  # incrementation of this value in the while to use it properly
        while period == -1:
            if hour == hourList[incHour] and minute > minuteList[incHour] or hour == \
            hourList[incHour] and minute <= minuteList[incHour]:
                period = incHour
            else:
                incHour += 1
        if period != 0:
            period -= 1
    if debug == True:
        print(f"[DEBUG] Day: {currentDay} Period: {period} Hour: {hour} Minute: {minute} ClassRole: {schoolRole}")

    for jour in range(7):  # because there are 7 day in a week
        if currentDay == jour:  # this way i use the day i got as an useful variable
            theLeftOfUs: int = -1  # value to increment to give us the remaining courses
            titleEmbed = f"Horaire {jour_semaine[currentDay].capitalize()}\n"
            descriptionEmbed = ""
            for heurePeriod in range(8 - period):  # because i only want the bot to print today's remaining courses
                theLeftOfUs += 1
                descriptionEmbed += (
                    f"\n {heurePeriod + period + 1}h {schoolTimetableArray[schoolRole][currentDay][period + theLeftOfUs]}")
            descriptionEmbed += (
                f"\n\n{pourcentage(0)}% de la journée scolaire est écoulé et {pourcentage(1)}% de la journée est écoulé")
            embed=discord.Embed(title=titleEmbed, description=descriptionEmbed, color=0xf48224)
            embed.set_author(name=
                f"{ctx.message.author.display_name} ({classesFromConfig[schoolRole]})", icon_url=ctx.message.author.avatar_url)
            embed.set_footer(text="Powered by KIYU Industries")
            return embed


@bot.command(name="horaire")
async def timetable(ctx, jour=None):
    if jour == None:
        dayWeek = date.today()  # get day as a string
        currentDay = date.weekday(dayWeek)  # get day in integrer 0=monday,1=tuesday,...
        nowPreciseDate = datetime.now()  # get exact date with seconds
        await ctx.send(
            embed=sendHoraire(ctx, int(nowPreciseDate.strftime("%M")), int(nowPreciseDate.strftime("%H")), currentDay))
        if debug:
            print(f"[DEBUG] !horaire : Today timetable printed in channel ID {ctx.channel.id}")
    else:
        for x in range(len(jour_semaine)):
            if jour == jour_semaine[x]:
                if x == 5 or x == 6:
                    await ctx.send(
                        "Où est-ce que tu vois qu'on à école ? **T'es con ou quoi ?**",
                        file=discord.File("Assets\images\myschoolweek_fr.jpg"))
                    print(
                        (f"[DEBUG] !horaire : {jour_semaine[x]} joke"
                        f"printed in channel ID {ctx.channel.id}"))
                else:
                    await ctx.send(embed=sendHoraire(ctx, 0, 6, x))
                    print(
                        (f"[DEBUG] !horaire : {jour_semaine[x]} timetable"
                         f"printed in channel ID {ctx.channel.id}"))
    await asyncio.sleep(5)
    await ctx.message.delete()


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

    authorizedMembers = {225282512438558720}
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
        "Il semblerait que oui", "Il semblerait que non...",
        "La réponse pourrait vous choquer... "]
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
        ("Tu sais combien de temps ça ma pris pour coder tout ça ?"
         " moins que ça t'aurait pris pour corriger ce message"),
        "Je te chie dessus depuis l'espace", "kinda cringe bro", 
        "Mec tu me fais quoi là", "Apprend", "Hérétique!!!",
        "J'arrive te niquer prépare ton cul", 
        "Tu sais même pas écrire une commande", 
        "J'ai même plus envie de répondre",
        "Pourquoi t'es encore sur ce discord, on t'a toujours ban ?",
        "**soupir**","CHALLENGE:JE FERME MA GUEULE PENDANT 24HEURES!!! (ça tourne mal!!)"]
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
    #/!\ I DID NOT WRITE THIS CODE HERE IS THE GITHUB REPO FORM WHERE IT COME FROM
    #https://github.com/peterlravn/My-projects
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

bot.run("")
