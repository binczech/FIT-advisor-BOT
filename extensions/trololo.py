import discord
from discord.ext import commands, tasks
import random

stornoMessages = [
    "Bohužel na toto mohu jen odpovědět, že na FITu toto nelze.",
    "Nevím, jak to je jinde, ale u nás to prostě nejde.",
    "V tuto chvíli to na FITu neumíme",
]

class Trololo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message: discord.message):
        print(message)
        if ("storno" in message.content.lower() and not message.author.bot):
            newMessage = f'{message.author.mention} Storno nebude.'
            await message.channel.send(newMessage)
        elif ("distan" in message.content.lower() and not message.author.bot):
            newMessage = f'{message.author.mention} Distanční výuku nám neumožňuje zákon.'
            await message.channel.send(newMessage)
        elif ("veigend" in message.content.lower() and message.author.id == 340810272929480705):
            newMessage = f'{message.author.mention} Pane kolego, držte píču.'
            await message.channel.send(newMessage)
        elif ("veigend" in message.content.lower() and not message.author.bot):
            newMessage = f'{message.author.mention} Ano, jsem zde, co je třeba?'
            await message.channel.send(newMessage)
        elif ("magist" in message.content.lower() and not message.author.bot):
            newMessage = f'{message.author.mention} Naše magisterské je velice zajímavé a nabídne kvalitní přípravu do praxe.'
            await message.channel.send(newMessage)
        elif ("pls url na prestižní školu" in message.content):
            newMessage = "https://www.fi.muni.cz/"
            await message.channel.send(newMessage)
        elif (("prestiz" in message.content.lower() or "prestiž" in message.content.lower()) and not message.author.bot):
            newMessage = f'{message.author.mention} Prestiž? To musíte asi mluvit o nejlepší IT škole v ČR.'
            await message.channel.send(newMessage)
        elif (f'<@!{self.bot.user.id}>' in message.content and "bajkař" in message.content.lower()):
            newMessage = f'{message.author.mention} Nejlepší student, který nám na FITu tuze chybí!'
            await message.channel.send(newMessage)
        elif (f'<@!{self.bot.user.id}>' in message.content and "lgtm" in message.content.lower()):
            newMessage = f'{message.author.mention} Jeho přechod na FI MUNI zvýšil oběma školám prestiž.'
            await message.channel.send(newMessage)
        elif ("toaster" in message.content.lower()  and not message.author.bot):
            newMessage = f'{message.author.mention} Toaster... Co k tomu říct... Každá škola prostě musí být alespoň trochu inkluzivní.'
            await message.channel.send(newMessage)
        elif (f'<@!{self.bot.user.id}>' in message.content and "medde" in message.content.lower()):
            newMessage = f'{message.author.mention} Medde co?'
            await message.channel.send(newMessage)
        elif (f'<@!{self.bot.user.id}>' in message.content):
            newMessage = f'{message.author.mention} {random.choice(stornoMessages)}'
            await message.channel.send(newMessage)
        

def setup(bot):
    bot.add_cog(Trololo(bot))
