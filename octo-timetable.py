import discord
import random
from discord.ext import commands
from datetime import date, datetime
import yaml

debug = False # to get more precise information in the log

bot = commands.Bot(command_prefix="!")

mon4A = ["Géographie", "Math", "Sciences", "Anglais", "Français", "Religion", "Anglais", "Math"]
tue4A = ["Histoire", "Religion", "Option (je sais pas mec)", "Math", "Math", "Langue 2", "Informatique/Étude",
         "Informatique/Étude"]
wed4A = ["Math", "Français", "Français", "Option (je sais pas mec)", "Langue 1", "/", "/", "/"]
thu4A = ["Histoire", "Sciences", "Français", "Langue 2", "Sport", "Langue 1", "Informatique/Étude",
         "Informatique/Étude"]
fri4A = ["Étude", "Géographie", "Sciences", "Français", "Langue 1", "Sport", "Allemand/Étude", "Allemand/Étude"]
the4A = [mon4A, tue4A, wed4A, thu4A, fri4A, mon4A, mon4A]

mon4B = ["Latin/Étude", "Sport intensif", "Sport intensif", "Anglais", "Sciences", "Latin/Étude", "Religion",
         "Géographie/Anglais"]
tue4B = ["Math", "Histoire/Anglais", "Math", "Sciences", "Anglais/Histoire", "Allemand/Étude", "Français", "Français"]
wed4B = ["Sciences", "Math", "Anglais/Histoire", "Latin/Étude", "Anglais/Géographie", "/", "/", "/"]
thu4B = ["Math", "Histoire/Anglais", "Géographie/Anglais", "Allemand/Étude", "Français", "Français", "Math", "Étude"]
fri4B = ["Labo", "Labo", "Français", "Anglais", "Latin/Étude", "Religion", "Allemand/Étude", "Allemand/Étude"]
the4B = [mon4B, tue4B, wed4B, thu4B, fri4B, mon4B, mon4B]

mon4D = ["Latin/Étude", "Math", "Math", "Géographie", "Étude", "Latin/Étude", "Sciences", "Anglais"]
tue4D = ["Math", "Anglais", "Français", "Religion", "Histoire", "Allemand/Étude", "Sport/Info", "Sport/Info"]
wed4D = ["Religion", "Français", "Histoire", "Latin/Étude", "Géographie", "/", "/", "/"]
thu4D = ["Math", "Anglais", "Anglais", "Allemand/Étude", "Faire des squats", "Français", "Science", "Français"]
fri4D = ["Sciences", "Français", "Math", "Anglais", "Latin/Étude", "Faire des pompes", "Allemand/Étude",
         "Allemand/Étude"]
the4D = [mon4D, tue4D, wed4D, thu4D, fri4D, mon4D, mon4D]

mon4E = ["Math", "**Faire la saucisse**", "**Faire des roulades à la zelda", "Géographie", "Religion", "Sciences",
         "Sciences", "Anglais"]
tue4E = ["Français", "Anglais", "Sciences", "Français", "Histoire", "Allemand/Étude", "Étude", "Étude"]
wed4E = ["Français", "Math", "Histoire", "Sciences", "Géographie", "/", "/", "/"]
thu4E = ["Étude", "Anglais", "Anglais", "Allemand/Étude", "Religion", "Math", "Informatique/Étude",
         "Informatique/Étude"]
fri4E = ["Français", "Math", "Math", "Anglais", "Sciences", "Français", "Allemand/Étude", "Allemand/Étude"]
the4E = [mon4E, tue4E, wed4E, thu4E, fri4E, mon4E, mon4E]

mon4F = ["Religion", "Histoire", "Français", "Français", "Math", "Sciences", "Sciences", "Étude"]
tue4F = ["Histoire", "Anglais", "Sciences", "**Faire des abdos**", "**Muscler son boule**", "Allemand/Étude", "Étude",
         "Étude"]
wed4F = ["Anglais", "Math", "Math", "Sciences", "Français", "/", "/", "/"]
thu4F = ["Géographie", "Français", "Anglais", "Allemand/Étude", "Religion", "Math", "Informatique", "Informatique"]
fri4F = ["Anglais", "Anglais", "Math", "Géographie", "Sciences", "Français", "Allemand/Étude", "Allemand/Étude"]
the4F = [mon4F, tue4F, wed4F, thu4F, fri4F, mon4F, mon4F]

mon4G = ["Étude", "Comms", "Comms", "**Sport**", "Soulever des ~~bites~~ poids", "Anglais", "Math", "Math"]
tue4G = ["Science", "AHV", "Rel", "\"**Sport**\"", "\"**Sport**\"", "Sciences", "Histoire-Géo", "Flute"]
wed4G = ["IVP", "EVS", "EVS", "Anglais", "Étude", "/", "/", "/"]
thu4G = ["AHV", "Français", "Français", "**Kazoo**", "Religion", "Math", "Anglais", "Histoire-Géo"]
fri4G = ["AHV", "IVP", "IVP", "Math", "Français", "Français", "Anglais", "Étude"]
the4G = [mon4G, tue4G, wed4G, thu4G, fri4G, mon4G, mon4G]
schoolTimetableArray = [the4A, the4B, the4D, the4E, the4F, the4G]

jour_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi",
                "dimanche"]  # I define each day of the week


@bot.event
async def on_ready():  # print in the console when bot wake up
    print("[INFO] Bot started and initialized as excepted")
    await bot.change_presence(activity=discord.Game("manger des bambous là"))

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


def sendHoraire(ctx, minute, hour, current_day):
    schoolRole = 0  # need to be referenced before assignement
    classesFromConfig = yaml.load(open("config.yaml"), Loader=yaml.FullLoader).get("classes")
    role4A, role4B, role4D, role4E, role4F, role4G = "","","","","",""
    schoolRoleArray = [role4A, role4B, role4D, role4E, role4F, role4G]
    for y in range(len(classesFromConfig)):
        schoolRoleArray[y] = discord.utils.get(ctx.guild.roles, name=classesFromConfig[y])
    for ima in range(len(classesFromConfig)):
        if schoolRoleArray[ima] in ctx.author.roles:
            schoolRole = ima

    period = -1
    if current_day > 4:
        period = 0
        current_day = 0
    elif hour >= 16 or hour == 15 and minute > 55:
        period = 0
        current_day += 1
    elif hour < 8:
        period = 0
    else:
        incHour = 0  # incrementation of this value in the while to use it properly
        hourList = yaml.load(open("config.yaml"), Loader=yaml.FullLoader).get("hours")
        minuteList = yaml.load(open("config.yaml"), Loader=yaml.FullLoader).get("minutes")
        while period == -1:
            if hour == hourList[incHour] and minute > minuteList[incHour] or hour == hourList[incHour] and minute <= \
                    minuteList[incHour]:
                period = incHour
            else:
                incHour += 1
        if period != 0:
            period -= 1
    if debug == True:
        print("[DEBUG] Day:", current_day, "Period:", period, "Hour:", hour, "Minute:", minute, "ClassRole:",
              schoolRole)

    preciseDate = datetime.now()  # get a reference of hours/minutes now to have the right value
    for jour in range(7):  # because there are 7 day in a week
        if current_day == jour:  # this way i use the day i got as an useful variable
            theLeftOfUs = -1  # value to increment to give us the remaining courses
            toPrint = ("```Horaire "+classesFromConfig[schoolRole]+" "+jour_semaine[current_day].capitalize()+ " :\n")
            for heurePeriod in range(8 - period):  # because i only want the bot to print today's remaining courses
                theLeftOfUs += 1
                toPrint += ("\n" + str(heurePeriod + period + 1) + "h " + schoolTimetableArray[schoolRole][current_day][
                    period + theLeftOfUs])
            toPrint += ("\n\n" + pourcentage(0) + "% de la journée scolaire est écoulé et " + pourcentage(
                1) + "% de la journée est écoulé```")
            return toPrint


@commands.guild_only()
@bot.command(name="horaire")
async def timetable(ctx, jour=None):
    if jour == None:
        dayWeek = date.today()  # get day as a string
        current_day = date.weekday(dayWeek)  # get day in integrer 0=monday,1=tuesday,...
        nowPreciseDate = datetime.now()  # get exact date with seconds
        await ctx.send(
            sendHoraire(ctx, int(nowPreciseDate.strftime("%M")), int(nowPreciseDate.strftime("%H")), current_day))
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
async def Mails(ctx):
    for a in range(1):
        RandomMail = str(random.randrange(1, 12))
    await ctx.send(file=discord.File("Assets\images\MailsDB\MailZeippen"+RandomMail+".png"))
    if debug == True:
        print("[DEBUG] !mails : Image "+RandomMail+" printed in channel ID "+str(ctx.channel.id))

@bot.command(name="bamboula")
async def Bamboula(ctx):
    await ctx.send("https://youtu.be/Agtyo-Rem3Q")

@bot.command(name="love")
async def Love(ctx, Personne1, Personne2):
    printIt = 1

    wordBanList = ['@everyone', '@here', '<@&763489250162507809>','<@&777564025432965121>','<@&822200827347075132>',
                   '<@&763815680306184242>','<@&764422266560839680<','<@&763815728972300338>','<@&763815728972300338>'
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

@bot.command(
    aliases=["orraire", "horraire", "orairre", "horairre", "horzire", "orair", "oraire", "horair", "haraire", "horarie",
             "hroaire", "hraire", "hauraire", "haurair", "haurer"])
async def Insultes(ctx):
    insultes = ["Apprend à écrire gros con", "**issou**", "Tu écris comme Prem", "Y'a de l'autisme dans l'air la non ?",
                "quelle orthographe dis donc", "Pire que Manon Boegen", "ew",
                "https://www.jaitoutcompris.com/rubriques/dictionnaire.php",
                "https://www.amazon.fr/Dictionnaire-Robert-Junior-illustré-CE-CM-6e/dp/2321015160/ref=sr_1_1",
                "Tu sais combien de temps ça ma pris pour codé tout ça ? moins que ça t'aurait pris pour corriger ce message",
                "Je te chie dessus depuis l'espace", "kinda cringe bro", "Mec tu me fais quoi là", "Apprend","Hérétique!!!",
                "J'arrive te niquer prépare ton cul", "Tu sais même pas écrire une commande"]
    await ctx.send(random.choice(insultes))

bot.run("")