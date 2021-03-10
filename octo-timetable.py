import discord
import random
from discord.ext import commands
from datetime import date, datetime
import yaml
bot = commands.Bot(command_prefix="!", description="Devant la librarie")

mon4A = ["Géographie", "Math", "Sciences", "Anglais", "Français","Religion","Anglais", "Math"]
tue4A = ["Histoire", "Religion", "Option fils de pute", "Math", "Math", "Langue 2", "Info/étude", "Info/étude"]
wed4A = ["Math", "Français", "Français", "Option fils de pute", "Langue 1", "Rien", "Rien", "Rien"]
thu4A = ["Histoire", "Sciences", "Français", "Langue 2", "Sport", "Langue 1", "Info/étude", "Info/étude"]
fri4A = ["étude", "Géographie", "Sciences", "Français", "Langue 1", "Sport", "Allemand/étude", "Allemand/étude"]
the4A = [mon4A, tue4A, wed4A, thu4A, fri4A, mon4A, mon4A]

mon4B = ["Latin/étude", "Sport intensif", "Sport intensif", "Anglais", "Sciences", "Latin/étude", "Religion", "Géographie/Anglais"]
tue4B = ["Math", "Histoire/Anglais", "Math", "Sciences", "Anglais/Histoire", "Allemand/étude", "Français", "Français"]
wed4B = ["Sciences", "Math", "Anglais/Histoire", "Latin/étude", "Anglais/Géographie", "Rien", "Rien", "Rien"]
thu4B = ["Math", "Histoire/Anglais", "Géographie/Anglais", "Allemand/étude", "Français", "Français", "Math", "étude"]
fri4B = ["Labo", "Labo", "Français", "Anglais", "Latin/étude", "Religion", "Allemand/étude", "Allemand/étude"]
the4B = [mon4B, tue4B, wed4B, thu4B, fri4B, mon4B, mon4B]

mon4D = ["Latin/étude", "Math", "Math", "Géographie", "étude", "Latin/étude", "Sciences", "Anglais"]
tue4D = ["Math", "Anglais", "Français", "Religion", "Histoire", "Allemand/étude", "Sport/Info", "Sport/Info"]
wed4D = ["Religion", "Français", "Histoire", "Latin/étude", "Géographie", "Rien", "Rien", "Rien"]
thu4D = ["Math", "Anglais", "Anglais", "Allemand/étude", "Faire des squats", "Français", "Science", "Français"]
fri4D = ["Sciences", "Français", "Math", "Anglais", "Latin/étude", "Faire des pompes", "Allemand/étude", "Allemand/étude"]
the4D = [mon4D, tue4D, wed4D, thu4D, fri4D, mon4D, mon4D]

mon4E = ["Math", "**Faire la saucisse**", "**Faire des roulades à la zelda", "Géographie", "Religion", "Sciences", "Sciences", "Anglais"]
tue4E = ["Français", "Anglais", "Sciences", "Français", "Histoire", "Allemand/étude", "étude", "étude"]
wed4E = ["Français", "Math", "Histoire", "Sciences", "Géographie", "Rien", "Rien", "Rien"]
thu4E = ["étude", "Anglais", "Anglais", "Allemand/étude", "Religion", "Math", "Informatique/étude", "Informatique/étude"]
fri4E = ["Français", "Math", "Math", "Anglais", "Sciences", "Français", "Allemand/étude", "Allemand/étude"]
the4E = [mon4E, tue4E, wed4E, thu4E, fri4E, mon4E, mon4E]

mon4F = ["Religion", "Histoire", "Français", "Français", "Math", "Sciences", "Sciences", "étude"]
tue4F = ["Histoire", "Anglais", "Sciences", "**Faire des abdos**", "**Muscler son boule**", "Allemand/étude", "étude", "étude"]
wed4F = ["Anglais", "Math", "Math", "Sciences", "Français", "Rien", "Rien", "Rien"]
thu4F = ["Géographie", "Français", "Anglais", "Allemand/étude", "Religion", "Math", "Informatique", "Informatique"]
fri4F = ["Anglais", "Anglais", "Math", "Géographie", "Sciences", "Français", "Allemand/**étude", "Allemand/étude**"]
the4F = [mon4F, tue4F, wed4F, thu4F, fri4F, mon4F, mon4F]

mon4G = ["étude", "Comms", "Comms", "**Sport**", "Soulever des ~~bites~~ poids", "Anglais", "Math", "Math"]
tue4G = ["Science", "AHV", "Rel", "\"**Sport**\"", "\"**Sport**\"", "Sciences", "Histoire-Géo", "Flute"]
wed4G = ["IVP", "EVS", "EVS", "Anglais", "étude", "Rien", "Rien", "Rien"]
thu4G = ["AHV", "Français", "Français", "**Kazoo**", "Religion", "Math", "Anglais", "Histoire-Géo"]
fri4G = ["AHV", "IVP", "IVP", "Math", "Français", "Français", "Anglais", "étude"]
the4G = [mon4G, tue4G, wed4G, thu4G, fri4G, mon4G, mon4G]
# array of timetable by classes adapt at your own need i personnaly have a classes each 50 minutes
schoolTimetableArray = [the4A, the4B, the4D, the4E, the4F, the4G]
# need to be in an array to be incremented later

@bot.event
async def on_ready():  # print in the console when bot wake up
    print("J'suis devant la libraire")
    await bot.change_presence(activity=discord.Game("invoquer skouizi"))


def pourcentage(h,m):
    toPourcent = h * 60 + m
    if toPourcent <= 480:
        return str(0)
    elif 480 > toPourcent or toPourcent < 955:
        toPourcent = (toPourcent - 480)/475 * 100
        return str(round(toPourcent,1))
    else:
        return str(100)

def sendHoraire(ctx,minute,hour,current_day):

    schoolRole = 0  # need to be referenced before assignement
    role4A = discord.utils.get(ctx.guild.roles, name="4A")
    role4B = discord.utils.get(ctx.guild.roles, name="4B")
    role4D = discord.utils.get(ctx.guild.roles, name="4D")
    role4E = discord.utils.get(ctx.guild.roles, name="4E")
    role4F = discord.utils.get(ctx.guild.roles, name="4F")
    role4G = discord.utils.get(ctx.guild.roles, name="4G")
    schoolRoleArray = [role4A, role4B, role4D, role4E, role4F, role4G]
    for ima in range(6):
        if schoolRoleArray[ima] in ctx.author.roles:
            schoolRole = ima #  to get the class the user is in, here i have set it to 6 because i have 6 possible classes

    if current_day > 4:  #in case we are the weekend and need monday courses
        period = 0
        hour = 6
    elif hour <= 8 and minute <= 50:
        period = 0
    elif (hour == 8 and minute > 50) or (hour == 9 and minute <= 40):
        period = 1
    elif (hour == 9 and minute > 40) or (hour == 10 and minute <= 30):
        period = 2
    elif (hour == 10 and minute > 30) or (hour == 11 and minute <= 35):
        period = 3
    elif (hour == 11 and minute > 35) or (hour == 12 and minute <= 25):
        period = 4
    elif (hour == 12 and minute > 25) or (hour == 13 and minute <= 25):
        period = 5
    elif (hour == 13 and minute > 25) or (hour == 14 and minute <= 15):
        period = 5
    elif (hour == 14 and minute > 15) or (hour == 15 and minute <= 5):
        period = 6
    elif (hour == 15 and minute > 5) or (hour == 15 and minute <= 55):
        period = 7
    elif hour >= 16:
        period = 0
        current_day += 1
    else:
        period = 0
        current_day = 6
        # all of this is used to get what course you should be having
        # /!\ i recommend putting lunchtime into it
    print("Jour:", current_day, "Cours:", period, "Heure", hour, "Minutes:", minute, "Classe:", schoolRole)  # made for debug
    for jour in range(7):  # because there are 7 day in a week
        if current_day == jour:  #this way i use the day i got as an useful variable
            theLeftOfUs = -1  #value to increment to give us the remaining courses
            toPrint = ("```Tes prochains cours:")
            for heurePeriod in range(8-period): #because i only want the bot to print today's remaining courses
                theLeftOfUs += 1
                toPrint += ("\n" + str(heurePeriod+period+1) +"h " + schoolTimetableArray[schoolRole][current_day][period + theLeftOfUs])
            toPrint += ("\nOn est à "+pourcentage(hour,minute)+"% de la journée scolaire et "+str(round((hour*60+minute)/1440 * 100,1))+"% de la journée```")
            return toPrint

@commands.guild_only()
@bot.command(name="horaire")
async def timetable (ctx):
    dayWeek = date.today()  # get day as a string
    current_day = date.weekday(dayWeek)  # get day in integrer 0=monday,1=tuesday,...
    nowPreciseDate = datetime.now()  # get exact date with seconds
    hour = int(nowPreciseDate.strftime("%H")) + 1
    minute = int(nowPreciseDate.strftime("%M"))  # get minutes as an int
    await ctx.send(sendHoraire(ctx,minute,hour,current_day))

args = "" # I define a str var args to use in "horairejour"

jour_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"] #I define each day of the week
@commands.guild_only()
@bot.command(name="horairejour")
async def timetableTomorow (ctx, args: str):
    i = 0 #i = increment
    if(jour_semaine[5] == args or jour_semaine[6] == args):
        await ctx.send("Où est-ce que tu vois qu'on à école ? **T'es con ou quoi ?**", file=discord.File("D:\Bureau\slt.jpg"))
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

bot.run("")