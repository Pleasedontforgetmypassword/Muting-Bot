import os
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# Gets Token
Token = os.environ.get('TOKEN')

# Gets the command prefix
Command = os.environ.get('COMMAND')

Dude = commands.Bot(command_prefix=Command)

Util = discord.utils


@Dude.event
async def on_ready():
    print(f"{Dude.user.name} is ready!")


@Dude.command(name="mute",
              help="Mutes a channel",
              usage=f"{Command}mute (voice channel name)")
async def mute(ctx, *, args):
    guild = ctx.guild
    Channel = Util.get(guild.channels, name=args)
    if ctx.author.guild_permissions.mute_members:
        for members in Channel.members:
            await members.edit(mute=True)
    else:
        await ctx.send(f"{ctx.author.mention}, You do not have Mute Members perms. You need Mute Members perms to use this command!")


@Dude.command(name="unmute",
              help="Unmutes a channel",
              usage=f"{Command}unmute (voice channel name)")
async def unmute(ctx, *, args):
    guild = ctx.guild
    Channel = Util.get(guild.channels, name=args)
    if ctx.author.guild_permissions.mute_members:
        for members in Channel.members:
            await members.edit(mute=False)
    else:
        await ctx.send(f"{ctx.author.mention}, You do not have Mute Members perms. You need Mute Members perms to use this command!")


@Dude.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title="Oops",
                          description=f"{ctx.author.mention}, You have used this command incorrectly, please refer to {Command}help for help")
    if isinstance(error, commands.errors.CommandInvokeError):
        embed.add_field(name='Error',
                        value=error)
        await ctx.send(embed=embed)


Dude.run(Token)
