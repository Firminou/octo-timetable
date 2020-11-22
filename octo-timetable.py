import discord
from discord.ext import commands
from datetime import date, datetime
bot = commands.Bot(command_prefix="!", description="Devant la librarie")
# you understand pretty explicit

mon4A = ["écoute moi bien", "tu me donnes ton horaire tout de suite", "j'ai ta mere en otage", "le bot est off mais j'ai interet a l'avoir demain", "vous avez compris la 4A ?", "", "", ""]
tue4A = ["", "", "", "", "", "Allemand/**étude**", "", ""]
wed4A = ["", "", "", "", "", "**Rien**", "**Rien**", "**Rien**"]
thu4A = ["", "", "", "Allemand/**étude**", "", "", "", ""]
fri4A = ["", "", "", "", "", "", "Allemand/**étude**", "Allemand/**étude**"]
the4A = [mon4A, tue4A, wed4A, thu4A, fri4A, mon4A, mon4A]

mon4B = ["Latin/**étude**", "**Sport intensif**", "**Sport intensif**", "Anglais", "Sciences", "Latin/**étude**", "Religion", "Géographie"]
tue4B = ["Math", "Histoire", "Math", "Sciences", "Anglais", "Allemand/**étude**", "Français", "Français"]
wed4B = ["Sciences", "Math", "Anglais", "Latin/**étude**", "Anglais", "**Rien**", "**Rien**", "**Rien**"]
thu4B = ["Math", "Histoire", "Géographie", "Allemand/**étude**", "Français", "Français", "Math", "**étude**"]
fri4B = ["Labo", "Labo", "Français", "Anglais", "Latin/**étude**", "Religion", "Allemand/**étude**", "Allemand/**étude**"]
the4B = [mon4B, tue4B, wed4B, thu4B, fri4B, mon4B, mon4B]

mon4D = ["Latin/**étude**", "Math", "Math", "Géographie", "**étude**", "Latin/**étude**", "Sciences", "Anglais"]
tue4D = ["Math", "Anglais", "Français", "Religion", "Histoire", "Allemand/**étude**", "Sport/Info", "Sport/Info"]
wed4D = ["Religion", "Français", "Histoire", "Latin/**étude**", "Géographie", "**Rien**", "**Rien**", "**Rien**"]
thu4D = ["Math", "Anglais", "Anglais", "Allemand/**étude**", "**Faire des squats**", "Français", "Science", "Français"]
fri4D = ["Sciences", "Français", "Math", "Anglais", "Latin/**étude**", "**Faire des pompes**", "Allemand/**étude**", "Allemand/**étude**"]
the4D = [mon4D, tue4D, wed4D, thu4D, fri4D, mon4D, mon4D]

mon4E = ["Math", "**Faire la saucisse**", "**Faire des roulades à la zelda", "Géographie", "Religion", "Sciences", "Sciences", "Anglais"]
tue4E = ["Français", "Anglais", "Sciences", "Français", "Histoire", "Allemand/**étude**", "**étude**", "**étude**"]
wed4E = ["Français", "Math", "Histoire", "Sciences", "Géographie", "**Rien**", "**Rien**", "**Rien**"]
thu4E = ["**étude**", "Anglais", "Anglais", "Allemand/**étude**", "Religion", "Math", "Informatique/**étude**", "Informatique/**étude**"]
fri4E = ["Français", "Math", "Math", "Anglais", "Sciences", "Français", "Allemand/**étude**", "Allemand/**étude**"]
the4E = [mon4E, tue4E, wed4E, thu4E, fri4E, mon4E, mon4E]

mon4F = ["Religion", "Histoire", "Français", "Français", "Math", "Sciences", "Sciences", "**étude**"]
tue4F = ["Histoire", "Anglais", "Sciences", "**Faire des abdos**", "**Muscler son boule**", "Allemand/**étude**", "**étude**", "**étude**"]
wed4F = ["Anglais", "Math", "Math", "Sciences", "Français", "**Rien**", "**Rien**", "**Rien**"]
thu4F = ["Géographie", "Français", "Anglais", "Allemand/**étude**", "Religion", "Math", "Informatique", "Informatique"]
fri4F = ["Anglais", "Anglais", "Math", "Géographie", "Sciences", "Français", "Allemand/**étude", "Allemand/étude**"]
the4F = [mon4F, tue4F, wed4F, thu4F, fri4F, mon4F, mon4F]

mon4G = ["**étude**", "Comms", "Comms", "**Sport**", "**Soulever des ~~bites~~ poids**", "Anglais", "Math", "Math"]
tue4G = ["Science", "AHV", "Rel", "\"**Sport**\"", "\"**Sport**\"", "Sciences", "Histoire-Géo", "**Flute**"]
wed4G = ["IVP", "EVS", "EVS", "Anglais", "**étude**", "**Rien**", "**Rien**", "**Rien**"]
thu4G = ["AHV", "Français", "Français", "**Kazoo**", "Religion", "Math", "Anglais", "Histoire-Géo"]
fri4G = ["AHV", "IVP", "IVP", "Math", "Français", "Français", "Anglais", "**étude**"]
the4G = [mon4G, tue4G, wed4G, thu4G, fri4G, mon4G, mon4G]
# array of timetable by classes adapt at your own need i personnaly have a classes each 50 minutes
schoolTimetableArray = [the4A, the4B, the4D, the4E, the4F, the4G]
# need to be in an array to be incremented later

@bot.event
async def on_ready():  # print in the console when bot wake up
    print("J'suis devant la libraire")
    await bot.change_presence(activity=discord.Game("péter sur des minorités"))

@commands.guild_only()
@bot.command(name="horaire")
async def timetable (ctx):
    dayWeek = date.today()  # get day as a string
    current_day = date.weekday(dayWeek)  # get day in integrer 0=monday,1=tuesday,...
    nowPreciseDate = datetime.now()  # get exact date with seconds
    hour = int(nowPreciseDate.strftime("%H"))  #- 1 # get hours as an int I REMOVE ONE HOUR CAUSE OF A DAMN RASPBERRY PI
    minute = int(nowPreciseDate.strftime("%M"))  # get minutes as an int

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
            schoolRole = ima
            #  to get the class the user is in here i have set it to 6 because i have 6 possible classes
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
    elif hour > 16:
        period = 0
        current_day += 1
    else:
        period = 0
        current_day = 6  # all of this is used to get what course you should be having
                         # /!\ i recommend puting lunchtime into it
    print("Jour:", {current_day}, "Cours:", {period}, "Heure", {hour}, "Minutes:", {minute}, "Classe:", {schoolRole})  # made for debug
    for jour in range(7):  # because there are 7 day in a week
        if current_day == jour:  #this way i use the day i got as an useful variable
            theLeftOfUs = -1  #value to increment to give us the remaining courses
            toPrint = ("Tes prochains cours sont dans :")
            for heurePeriod in range(8-period): #beacause i only want the bot to print today's remaining courses
                theLeftOfUs += 1
                toPrint += ("\n" + str(heurePeriod+1) +"h " + schoolTimetableArray[schoolRole][current_day][period + theLeftOfUs])
            await ctx.send(toPrint)
bot.run("YourDiscordToken")