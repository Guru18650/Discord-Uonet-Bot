from time import strftime, strptime
import discord, vulcan, asyncio
from datetime import date
import datetime
from datetime import datetime

class lessonClass: 
    def __init__(self, position, name, teacher_name, time_from, group): 
        self.position = position 
        self.name = name
        self.teacher_name = teacher_name
        self.time_from = time_from
        self.group = group

class gradeClass:
    def __init__(self, subject, mark, weight):
        self.subject = subject
        self.mark = mark
        self.weight = weight
        
async def GetTimetableEmbed(c, dateArg):
    if dateArg == "":
        data = datetime.now()
    else:
        data = datetime.strptime(dateArg, '%d.%m.%y')
    lessonsArray = []
    lessons = await c.data.get_lessons(date_from = data)
    embed=discord.Embed(title="Plan lekcji", description=date.today(), color=0x5900ff) 
    async for lesson in lessons:
        lessonbuffer = (str(lesson.group)[:str(lesson.group).rfind("', name")])
        group = lessonbuffer[len(lessonbuffer) - 2:]
        lessonsArray.append(lessonClass(lesson.time.position, lesson.subject.name, lesson.teacher.display_name, str(lesson.time.from_), group))
    lessonsArray.sort(key=lambda x: x.position)
    if len(lessonsArray) == 0:
        embed.add_field(name="Nie znaleziono lekcji", value=":(")
    for lessonA in lessonsArray:
        if(lessonA.group == "G1" or lessonA.group =="G2"):
            embed.add_field(name=str(lessonA.position) + ". " + str(lessonA.name) + " " + lessonA.group, value=lessonA.teacher_name + ", " + lessonA.time_from, inline=False)
        else:
            embed.add_field(name=str(lessonA.position) + ". " + str(lessonA.name) , value=lessonA.teacher_name + ", " + lessonA.time_from, inline=False) 
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed
        

async def GetLuckyNumberEmbed(c, dateArg):
    if dateArg == "":
        data = datetime.now()
    else:
        data = datetime.strptime(dateArg, '%d.%m.%y')
    lnumber = await c.data.get_lucky_number(data)
    nfinal = lnumber.number
    if nfinal == 0:
        nfinal = "Brak";
    embed=discord.Embed(title="Szczęśliwy numerek", description=str(str(data.date())+ " - **" + str(nfinal) + "**"), color=0x5900ff)
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed
    
async def GetGradesEmbed(c):
    gradesD = {}
    grades = await c.data.get_grades()
    embed=discord.Embed(title="Oceny", description=str(date.today()), color=0x5900ff) 
    async for gradeO in grades:
        if gradeO.column.subject not in gradesD:
            gradesD[gradeO.column.subject] = []
        gradesD[gradeO.column.subject].append(gradeO)
    for key in gradesD:
        gradeString = ""
        for grade in gradesD[key]:
            gradeString = gradeString + str(grade.value)[0] + ", "
            count+=1*grade.column.weight
            sum+=grade.value*grade.column.weight
        embed.add_field(name=grade.column.subject.name, value=gradeString[:len(gradeString) - 2], inline=True)
    embed.set_footer(text="SztefanoV3 by Migu2137")
    
    return embed

async def GetExamsEmbed(c):
    exams = await c.data.get_exams(last_sync = datetime(2022,9,1))
    embed=discord.Embed(title="Sprawdziany", description=str(date.today()), color=0x5900ff) 
    async for exam in exams:
        if(exam.deadline.date > date.today()):
            embed.add_field(name=exam.subject.name + " " + exam.type, value=str(exam.deadline.date) + " " + exam.topic, inline=True)
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed

async def GetHomeworkEmbed(c):
    homeworks = await c.data.get_homework(last_sync = datetime(2022,9,1))
    embed=discord.Embed(title="Zadania z UONET+", description=str(date.today()), color=0x5900ff) 
    async for homework in homeworks:
        if(homework.deadline.date > date.today()):
            embed.add_field(name=homework.subject.name + " - " + str(homework.deadline.date), value=homework.content, inline=False)
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed