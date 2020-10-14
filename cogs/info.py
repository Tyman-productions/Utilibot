import discord, random, asyncio, string
from discord.ext import commands
import datetime

def randcolor():
	return int("%06x" % random.randint(0, 0xFFFFFF), 16)

def permsfromvalue(value):
	perms = discord.Permissions(permissions=int(value))
	perms_true = sorted([x for x,y in dict(perms).items() if y])
	perms_false = sorted([x for x,y in dict(perms).items() if not y])
	nice_perms = ""
	perms_true = ["\u2705 `" + s for s in perms_true]
	perms_false = ["\u274c `" + s for s in perms_false]
	perms_combined = sorted(perms_true + perms_false, key=lambda x: x.strip('\u2705\u274c'))
	for perm in perms_combined:
		nice_perms = nice_perms + perm.replace("_", " ").capitalize() + "`\n"
	return nice_perms

class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def ping(self, ctx):
		"""
		Get the bot's latency, in miliseconds.
		"""
		if ctx.channel.permissions_for(ctx.me).embed_links == False:
			return await ctx.send("It appears I do not have permission to `Link embeds` in this channel. Please give me this permission or try in a channel where I do have it, as it is necessary to run this command.")
		embed1 = discord.Embed(title="Pong!", description=f"Given Latency:`{round(self.bot.latency * 1000)}ms`", color=randcolor())
		m = await ctx.send(embed=embed1)
		embed2 = embed1
		time = m.created_at - ctx.message.created_at
		embed2.description = f"Given Latency: `{round(self.bot.latency * 1000)}ms`\nMeasured Latency: `{int(time.microseconds / 1000)}ms`"
		await m.edit(embed=embed2)

	@commands.command()
	async def invite(self, ctx):
		"""
		Get the invite for the bot, and support server.
		"""
		if ctx.channel.permissions_for(ctx.me).embed_links == False:
			return await ctx.send("It appears I do not have permission to `Link embeds` in this channel. Please give me this permission or try in a channel where I do have it, as it is necessary to run this command.")
		embed = discord.Embed(title="Invite link", description="Click the links below to invite the bot to your server, or join our support server!\n[Click me to invite the bot!](https://discord.com/api/oauth2/authorize?client_id=755084857280954550&permissions=2147483639&redirect_uri=https%3A%2F%2Fdiscord.com&scope=bot)\n[Click me to join the support server!](https://discord.gg/Tbg3HDW)", color=randcolor())
		await ctx.send(embed=embed)
	
	@commands.command(name="botperms", aliases=['botpermissions'])
	@commands.has_permissions(manage_guild=True)
	async def _bot_permissions(self, ctx, channel_permissions="False"):
		"""
		Shows all of the bot's permissions, neatly sorted.

		channel_permissions = Whether or not to check the channel permissions, instead of the guild ones (default false)
		"""
		if ctx.channel.permissions_for(ctx.me).embed_links == False:
			return await ctx.send("It appears I do not have permission to `Link embeds` in this channel. Please give me this permission or try in a channel where I do have it, as it is necessary to run this command.")
		if channel_permissions.lower() == "true":
			await ctx.send(embed=discord.Embed(title="All of the bot's permissions in this channel (Permissions not able to be used in this type of channel will show as denied):", description=permsfromvalue(ctx.channel.permissions_for(ctx.me).value) + "\nRun `u!requiredperms` to see which ones the bot needs.", color=randcolor()))
		elif channel_permissions.lower() == "false":
			await ctx.send(embed=discord.Embed(title="All of the bot's permissions in this server:", description=permsfromvalue(ctx.me.guild_permissions.value) + "\nRun `u!requiredperms` to see which ones the bot needs.", color=randcolor()))

	@commands.command()
	async def requiredperms(self, ctx):
		if ctx.channel.permissions_for(ctx.me).embed_links == False:
			return await ctx.send("It appears I do not have permission to `Link embeds` in this channel. Please give me this permission or try in a channel where I do have it, as it is necessary to run this command.")
		embed=discord.Embed(title="Required permissions for the bot:", description="Necessary perms:\n`Read messages`, `Send messages`, `Embed links`\nPerms for commands to run:\n`Kick members`, `Ban members`, `Manage messages`, `Manage channels`", color=randcolor())
		await ctx.send(embed=embed)
	
	@commands.command()
	async def vote(self, ctx):
		embed = discord.Embed(title="Vote link:", description="You can vote for me [here](https://top.gg/bot/755084857280954550/vote)!").set_footer(text="Currently does not work because the bot is not approved on top.gg")	
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Info(bot))
	commands.HelpCommand.cog = Info(bot)
	print('[InfoCog] Info cog loaded')
