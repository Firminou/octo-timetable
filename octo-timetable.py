######################## SETTINGS ######################
debug = False
########################################################


import discord
import random
from discord.ext import commands
from datetime import date, datetime

import yaml


bot = commands.Bot(command_prefix="!")

mon4A = ["Géographie", "Math", "Sciences", "Anglais", "Français", "Religion", "Anglais", "Math"]
tue4A = ["Histoire", "Religion", "Option (je sais pas mec)", "Math", "Math", "Langue 2", "Informatique/Étude", "Informatique/Étude"]
wed4A = ["Math", "Français", "Français", "Option (je sais pas mec)", "Langue 1", "/", "/", "/"]
thu4A = ["Histoire", "Sciences", "Français", "Langue 2", "Sport", "Langue 1", "Informatique/Étude", "Informatique/Étude"]
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
        return str(round((((int(nowPreciseDate.strftime("%H"))) * 60 )+ (int(nowPreciseDate.strftime("%M")))) / 1440 * 100, 1))

def sendHoraire(ctx, minute, hour, current_day):
    schoolRole = 0  # need to be referenced before assignement
    classesFromConfig = yaml.load(open("config.yaml"), Loader=yaml.FullLoader).get("classes")
    role4A = discord.utils.get(ctx.guild.roles, name=classesFromConfig[0])
    role4B = discord.utils.get(ctx.guild.roles, name=classesFromConfig[1])
    role4D = discord.utils.get(ctx.guild.roles, name=classesFromConfig[2])
    role4E = discord.utils.get(ctx.guild.roles, name=classesFromConfig[3])
    role4F = discord.utils.get(ctx.guild.roles, name=classesFromConfig[4])
    role4G = discord.utils.get(ctx.guild.roles, name=classesFromConfig[5])
    schoolRoleArray = [role4A, role4B, role4D, role4E, role4F, role4G]
    for ima in range(6):
        if schoolRoleArray[ima] in ctx.author.roles:
            schoolRole = ima  # to get the class the user is in, here i have set it to 6 because i have 6 possible classes

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
        print("[DEBUG] Jour:", current_day, "Periode:", period, "Heure", hour, "Minutes:", minute, "Classe:",
            schoolRole)  # made for debug    

    preciseDate = datetime.now() #get a reference of hours/minutes now to have the right value
    for jour in range(7):  # because there are 7 day in a week
        if current_day == jour:  # this way i use the day i got as an useful variable
            theLeftOfUs = -1  # value to increment to give us the remaining courses
            toPrint = ("```Ton Horaire :")
            for heurePeriod in range(8 - period):  # because i only want the bot to print today's remaining courses
                theLeftOfUs += 1
                toPrint += ("\n" + str(heurePeriod + period + 1) + "H " + schoolTimetableArray[schoolRole][current_day][
                    period + theLeftOfUs])
            toPrint += ("\n" + pourcentage(0) + "% de la journée scolaire est écoulé et " + pourcentage(1) + "% de la journée est écoulé```")
            return toPrint

@commands.guild_only()
@bot.command(name="horaire")
async def timetable(ctx):
    dayWeek = date.today()  # get day as a string
    current_day = date.weekday(dayWeek)  # get day in integrer 0=monday,1=tuesday,...
    nowPreciseDate = datetime.now()  # get exact date with seconds
    await ctx.send(sendHoraire(ctx, int(nowPreciseDate.strftime("%M")), int(nowPreciseDate.strftime("%H")), current_day))

args = "" # I define a str var args to use in "horairejour"
jour_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"] #I define each day of the week
@commands.guild_only()
@bot.command(name="horairejour")
async def timetableTomorow (ctx, args: str):
    i = 0 #i = increment
    if(jour_semaine[5] == args or jour_semaine[6] == args):
        await ctx.send("Où est-ce que tu vois qu'on à école ? **T'es con ou quoi ?**", file=discord.File("Assets\images\myschoolweek_fr.jpg"))
    else:
        for i in range(5): #I'm checking each possible day of the week
            i += 1
            #await ctx.send("DEBUG : nb du for : "+str(i)+" jour insere : "+args+" jour vérifié : "+jour_semaine[i-1]) Debug functionnality (Do not use if you don't know what you're doing)
            if (args.lower() == jour_semaine[i-1]): 
                await ctx.send(sendHoraire(ctx,0,6,i-1))
                break
            elif(i == 5 and jour_semaine[4] != args): await ctx.send("Alors on connait pas les jours de la semaine ?")
            
            
            

@bot.command(aliases=["orraire","horraire","orairre","horairre","horzire","orair","oraire","horair","haraire","horarie","hroaire","hraire","hauraire","haurair","haurer"
"orrairejour","horrairejour","orairrejour","horairrejour","horzirejour","orairjour","orairejour","horairjour","harairejour","horariejour","hroairejour","hrairefour"])
async def x (ctx):
    insultes = ["Apprend à écrire gros con","**issou**","Tu écris comme Prem","Y'a de l'autisme dans l'air la non ?",
                "quelle orthographe dis donc","Pire que Manon Boegen","ew","https://www.jaitoutcompris.com/rubriques/dictionnaire.php",
                "https://www.amazon.fr/Dictionnaire-Robert-Junior-illustré-CE-CM-6e/dp/2321015160/ref=sr_1_1",
                "Tu sais combien de temps ça ma pris pour codé tout ça ? moins que ça t'aurait pris pour corriger ce message",
                "Je te chie dessus depuis l'espace","kinda cringe bro","Mec tu me fais quoi là","Apprend"]
    await ctx.send(random.choice(insultes))

bot.run("NzY0NDk0ODAyMjQyNzY0ODQw.X4HFRA.M59Z9eyrLcF07Np4CmTg_URFvZQ")