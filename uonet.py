import discord, vulcan, asyncio
from datetime import date

async def GetTimetableEmbed(c):
    lessons = await c.data.get_lessons()
    embed=discord.Embed(title="Plan lekcji", description=date.today(), color=0x5900ff) 
    async for lesson in lessons:
        lessonbuffer = (str(lesson.group)[:str(lesson.group).rfind("', name")])
        group = lessonbuffer[len(lessonbuffer) - 2:]
        if(group == "G1" or group =="G2"):
            embed.add_field(name=str(lesson.subject.name) + " " + group, value=lesson.teacher.display_name + ", " + str(lesson.time.from_), inline=False)
        else:
            embed.add_field(name=str(lesson.subject.name), value=lesson.teacher.display_name + ", " + str(lesson.time.from_), inline=False)
        
        
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed
        

async def GetLuckyNumberEmbed(c):
    lnumber = await c.data.get_lucky_number()
    embed=discord.Embed(title="Szczęśliwy numerek", description=str(lnumber.date) + " - **" + str(lnumber.number) + "**")
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed
    
async def GetGradesEmbed(c):
    grades = await c.data.get_grades()
    embed=discord.Embed(title="Oceny", description="data", color=0x5900ff) 
    async for grade in grades:
        embed.add_field(name=str(grade.column.subject.name), value=str(grade.value), inline=False)
        
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed