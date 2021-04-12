import discord
import random 
from discord.ext import commands
from datetime import datetime, date
import yaml
import asyncio

debug = False # to get more precise information in the log

botVersion = "1"

bot = commands.Bot(command_prefix="!")

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

jour_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi",
                "dimanche"]  # I define each day of the week


@bot.event
async def on_ready():  # print in the console when bot wake up
    print("[INFO] Bot initialized as excepted (botVersion = "+botVersion+")")
    await bot.change_presence(activity=discord.Game("!dumont"))

def pourcentage(mode):
    nowPreciseDate = datetime.now()  # get exact date with seconds
    toPourcent = (int(nowPreciseDate.strftime("%H"))) * 60 + int(nowPreciseDate.strftime("%M"))
    if mode == 0:
        if toPourcent <= 480:
            return str(0)
        elif 480 > toPourcent or toPourcent < 955:
            toPourcent = (toPourcent - 480) / 475 * 100
            return str(round(toPourcent, 1))
        else:
            return str(100)
    elif mode == 1:
        return str(
            round((((int(nowPreciseDate.strftime("%H"))) * 60) + (int(nowPreciseDate.strftime("%M")))) / 1440 * 100, 1))

def sendHoraire(ctx, minute, hour, currentDay):
    schoolRole = 0  # need to be referenced before assignement
    classesFromConfig = yaml.load(open("config.yaml"), Loader=yaml.FullLoader).get("classes")
    roleClass1, roleClass2, roleClass3, roleClass4, roleClass5, roleClass6 = "","","","","",""
    schoolRoleArray = [roleClass1, roleClass2, roleClass3, roleClass4, roleClass5, roleClass6]
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
            if hour == hourList[incHour] and minute > minuteList[incHour] or hour == hourList[incHour] and minute <= \
                    minuteList[incHour]:
                period = incHour
            else:
                incHour += 1
        if period != 0:
            period -= 1
    if debug == True:
        print("[DEBUG] Day:", currentDay, "Period:", period, "Hour:", hour, "Minute:", minute, "ClassRole:",
              schoolRole)

    preciseDate = datetime.now()  # get a reference of hours/minutes now to have the right value
    for jour in range(7):  # because there are 7 day in a week
        if currentDay == jour:  # this way i use the day i got as an useful variable
            theLeftOfUs = -1  # value to increment to give us the remaining courses
            toPrint = ("```Horaire "+classesFromConfig[schoolRole]+" "+jour_semaine[currentDay].capitalize()+ " :\n")
            for heurePeriod in range(8 - period):  # because i only want the bot to print today's remaining courses
                theLeftOfUs += 1
                toPrint += ("\n" + str(heurePeriod + period + 1) + "h " + schoolTimetableArray[schoolRole][currentDay][
                    period + theLeftOfUs])
            toPrint += ("\n\n" + pourcentage(0) + "% de la journée scolaire est écoulé et " + pourcentage(
                1) + "% de la journée est écoulé```")
            return toPrint

@bot.command(name="horaire")
async def timetable(ctx, jour=None):
    if jour == None:
        dayWeek = date.today()  # get day as a string
        currentDay = date.weekday(dayWeek)  # get day in integrer 0=monday,1=tuesday,...
        nowPreciseDate = datetime.now()  # get exact date with seconds
        await ctx.send(
            sendHoraire(ctx, int(nowPreciseDate.strftime("%M")), int(nowPreciseDate.strftime("%H")), currentDay))
        if debug == True:
            print("[DEBUG] !horaire : Today timetable printed in channel ID "+str(ctx.channel.id))
    else:
        for x in range(len(jour_semaine)):
            if jour == jour_semaine[x]:
                if x == 5 or x == 6:
                    await ctx.send("Où est-ce que tu vois qu'on à école ? **T'es con ou quoi ?**",
                                   file=discord.File("Assets\images\myschoolweek_fr.jpg"))
                    print("[DEBUG] !horaire : "+jour_semaine[x]+" joke printed in channel ID "+str(ctx.channel.id))
                else:
                    await ctx.send(sendHoraire(ctx, 0, 6, x))
                    print("[DEBUG] !horaire : "+jour_semaine[x]+" timetable printed in channel ID "+str(ctx.channel.id))

@bot.command(name="mails")
async def mails(ctx):
    for a in range(1):
        RandomMail = str(random.randrange(1, 12))
    await ctx.send(file=discord.File("Assets\images\MailsDB\MailZeippen"+RandomMail+".png"))
    if debug == True:
        print("[DEBUG] !mails : Image "+RandomMail+" printed in channel ID "+str(ctx.channel.id))
    await asyncio.sleep(5)
    await ctx.message.delete()

@bot.command(name="bamboula")
async def bamboula(ctx):
    await ctx.send("https://youtu.be/Agtyo-Rem3Q")
    await asyncio.sleep(5)
    await ctx.message.delete()

@bot.command(name="love", aliases=["l"])
async def love(ctx, Personne1, Personne2):
    if ctx.message.channel.id != 763352957579690018:
        printIt = 1
        wordBanList = ['@everyone', '@here', '<@&763489250162507809>','<@&777564025432965121>','<@&822200827347075132>',
                       '<@&763815680306184242>','<@&764422266560839680<','<@&763815728972300338>','<@&763815728972300338>',
                       '<@&763815228323528725>','<@&763815784904261632>','<@&764422166116171806>','<@&764422057353936897>',
                       '<@&804807279043674143>','<@&828664814678179861>','<@&823562218095640646>','<@&823638574809219163>']
        LoveRate = str(random.randrange(0, 100))
        for y in range(len(wordBanList)):
            if(Personne1 == wordBanList[y] or Personne2 == wordBanList[y]):
                printIt = 0

        if(printIt == 0):
            await ctx.send("Tu t'es pris pour qui ?")
            if debug == True:
                print("[DEBUG] !love : Someone tried to use a banned word !")
        else:
            await ctx.send("L'amour entre **"+Personne1+"** et **"+Personne2+"** est de **"+LoveRate+"%** <:flushed:830502924479758356>")
            if debug == True:
                print("[DEBUG] !love : The love rate ("+LoveRate+"%) between "+Personne1+" and "+Personne2+" has been printed in channel ID "+str(ctx.channel.id))
    else:
        botChannel = discord.utils.get(ctx.guild.channels, id=768194273970880533)
        messageBot = await ctx.send("Va faire cette commande dans "+botChannel.mention+" ou je te soulève <:rage:831149184895811614>")
        await asyncio.sleep(5)
        await ctx.message.delete()
        await messageBot.delete()

@bot.command(name="dumont")
async def dumont(ctx, userArgs: discord.Member = None):

    roleAdmin = discord.utils.get(ctx.guild.roles, name="*")
    roleMute = discord.utils.get(ctx.guild.roles, name="Mute")
    channelRetenue = discord.utils.get(ctx.guild.channels, id=769125453314261002)

    authorizedMembers = [225282512438558720]
    user = ctx.message.author

    await ctx.message.delete()
    
    if userArgs != None:
        for z in range(len(authorizedMembers)):
            if authorizedMembers[z] == user.id or roleAdmin in ctx.author.roles:
                user = userArgs
                await ctx.send(user.mention+" vient de se faire envoyer en retenue par Mr Dumont! <:angry:830881956870357023>")
            else:
                await ctx.send("Tu t'es cru où ? "+user.mention+", va en retenue! <:angry:830881956870357023>")
    else:
        await ctx.send(user.mention+" vient de se faire envoyer en retenue par Mr Dumont! <:angry:830881956870357023>")

    await user.add_roles(roleMute)
    if user.voice != None:
        await user.move_to(channelRetenue)
    await asyncio.sleep(180)
    await user.remove_roles(roleMute)

@bot.command(name="predict", aliases=["p"])
async def predict(ctx, args):
    if ctx.message.channel.id != 763352957579690018:
        predictE = "Prédiction <:crystal_ball:830965316468867082> : "

        predictPhrases = ["Oui","Non", "Peut-Être <:thinking:830966162824888320>",
                          "Je ne devrais peut-être pas le dire <:face_with_hand_over_mouth:831149509287084052>",
                          "Sans aucun doute", "C'est probable", "Je ne pense pas", "Probablement pas"
                          "Je ne suis pas sûr <:face_with_raised_eyebrow:831150009436995584>",
                          "Il semblerait que oui", "Il semblerait que non...","La réponse pourrait vous choquer... "]
        await ctx.send(predictE + "**"+random.choice(predictPhrases)+"**")

    else:
        botChannel = discord.utils.get(ctx.guild.channels, id=768194273970880533)
        messageBot = await ctx.send("Va faire cette commande dans "+botChannel.mention+" ou je te soulève <:rage:831149184895811614>")
        await asyncio.sleep(5)
        await ctx.message.delete()
        await messageBot.delete()

@bot.command(name="insultes", aliases=["orraire", "horraire", "orairre", "horairre", "horzire", "orair", "oraire", "horair", "haraire", "horarie",
                                       "hroaire", "hraire", "hauraire", "haurair", "haurer"])
async def insultes(ctx):
    insultes = ["Apprend à écrire gros con", "**issou**", "Tu écris comme Prem", "Y'a de l'autisme dans l'air la non ?",
                "quelle orthographe dis donc", "Pire que Manon Boegen", "ew",
                "https://www.jaitoutcompris.com/rubriques/dictionnaire.php",
                "https://www.amazon.fr/Dictionnaire-Robert-Junior-illustré-CE-CM-6e/dp/2321015160/ref=sr_1_1",
                "Tu sais combien de temps ça ma pris pour codé tout ça ? moins que ça t'aurait pris pour corriger ce message",
                "Je te chie dessus depuis l'espace", "kinda cringe bro", "Mec tu me fais quoi là", "Apprend","Hérétique!!!",
                "J'arrive te niquer prépare ton cul", "Tu sais même pas écrire une commande", "J'ai même plus envie de répondre",
                "Pourquoi t'es encore sur ce discord, on t'a toujours ban ?", ""]
    await ctx.send(random.choice(insultes))

bot.run("NzY0NDk0ODAyMjQyNzY0ODQw.X4HFRA.8RVS8XdY-VhSJKn1HnIFAXhq8LY")