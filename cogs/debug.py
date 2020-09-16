import discord, sys, os
from discord.ext import commands

async def is_owner(ctx):
	return ctx.author.id == 487443883127472129

class Debug(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.is_owner()
	async def quit(self, ctx):
		await ctx.send('Shutting down...')
		print('Recived quit command, shutting down.')
		sys.exit()

	@commands.command()
	@commands.is_owner()
	async def git(self, ctx, message="No message specified"):
		os.system(f'/home/pi/utilibot/git.sh {message}')

def setup(bot):
	bot.add_cog(Debug(bot))
	print('[DebugCog] Debug cog loaded')