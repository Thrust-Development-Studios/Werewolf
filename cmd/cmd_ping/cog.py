import nextcord
from nextcord.ext import commands


class PingCommand(commands.Cog, name='PingCommand'):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.commands(name='ping')
    async def ping(self, ctx: commands.Context):
        """A command which returns a ping response.
        Usage:
        ```
        -ping
        ```
        """

        await ctx.send('Pong!')