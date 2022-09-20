import discord, vulcan, asyncio

async def GetTimetableEmbed(c):
    lessons = await c.data.get_lessons()
    embed=discord.Embed(title="Plan lekcji", description="data", color=0x5900ff) 
    async for lesson in lessons:
        embed.add_field(name=str(lesson.subject.name) + " " + str(lesson.time.from_) + " - " + str(lesson.time.to), value=lesson.teacher.display_name, inline=False)
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed
        

async def GetLuckyNumberEmbed(c):
    lnumber = await c.data.get_lucky_number()
    embed=discord.Embed(title="Szczęśliwy numerek", description=str(lnumber.date) + " - **" + str(lnumber.number) + "**")
    embed.set_footer(text="SztefanoV3 by Migu2137")
    return embed
    