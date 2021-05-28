from discord.ext import commands

prefix = "prefix here"
token = "token here"
bot = commands.Bot(command_prefix=prefix, self_bot=True)


@bot.event
async def on_connect():
    print("Bot is now online!")


@bot.command()
async def clear(ctx, amount=100):
    await ctx.message.delete()
    async for msg in ctx.channel.history(limit=amount):
        if msg.author == bot.user:
            try:
                await msg.delete()
            except:
                pass


bot.run(token, bot=False)
