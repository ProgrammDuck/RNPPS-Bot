import discord
from discord.ext import commands
from discord.ui import Button, View
import logging

scemb = discord.Embed(
    title='✅ | Success',
    colour=discord.Colour.green()
)
eremb = discord.Embed(
    title='❌ | Error',
    colour=discord.Colour.red()
)

class owner(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.logger = logging.getLogger(__name__)
    
    #⁡⁢⁣⁣---𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀---⁡
    @commands.command('delete_message', hidden=True)
    @commands.is_owner()
    async def delete_message(self, ctx, message:discord.Message):
        await message.delete()

    @commands.command('send_message', hidden=True)
    @commands.is_owner()
    async def send_message(self, ctx, channelid, *, message):
        channel = await self.bot.fetch_channel(channelid)
        await channel.send(message)
    
    @commands.command(name='sync', hidden=True)
    @commands.is_owner()
    async def sync(self, ctx, id = None):
        if id:
            await self.bot.tree.sync(guild=discord.Object(id))
            logging.info('Syncing')
            msg = scemb.copy()
            msg.description = f'Synced the {id}'
            await ctx.reply(embed=msg, ephemeral=True)
        else:
            await self.bot.tree.sync()
            logging.info('Global Syncing ~ 1 hour')
            msg = scemb.copy()
            msg.description = f'Syncing | ~ 1 hour'
            await ctx.reply(embed=msg, ephemeral=True)
    
    
async def setup(bot):
    await bot.add_cog(owner(bot))