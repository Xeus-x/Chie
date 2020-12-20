import discord
import asyncio
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Help
    @commands.command()
    async def help(self, ctx, page = None):

        # Default
        help = discord.Embed(
            title = 'Help',
            description = "A list of all available commands.",
            color = discord.Color.red()
        )
        help.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help.add_field(
            name = 'Bot Status',
            value = "`ping`, `status`, `support`",
            inline = True
        )
        help.add_field(
            name = 'Moderation',
            value = "`clear_message`, `kick`, `ban`, `setprefix`",
            inline = True
        )
        help.add_field(
            name = 'Miscellaneous',
            value = "`say`, `8ball`, `throw`, `dice`, `choose`, `reputation`",
            inline = True
        )
        help.add_field(
            name = 'Economy',
            value = "`balance`, `transfer`, `daily`, `work`",
            inline = True
        )
        help.add_field(
            name = 'Fun/Action',
            value = "Temporarily Unavailable",
            inline = True
        )
        help.add_field(
            name = 'Profile',
            value = "`profile`, `inventory`, `bookshelf`",
            inline = True
        )
        help.add_field(
            name = 'Story',
            value = "`read`"
        )
        help.add_field(
            name = 'Guild House',
            value = "`train`, `commission`"
        )
        help.add_field(
            name = 'Detailed Page',
            value = "Just append the specific command you want to get the detailed information\n(e.g. `>help daily`.)",
            inline = False
        )

    ###########################################################################
    ###########################################################################

        # Ping
        help_ping = discord.Embed(
            title = 'Ping',
            color = discord.Color.red()
        )
        help_ping.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_ping.add_field(
            name = 'Aliases',
            value = 'None',
            inline = False
        )
        help_ping.add_field(
            name = 'Usage',
            value = "`ping`",
            inline = False
        )
        help_ping.add_field(
            name = 'Description',
            value = "Honestly, you know what it is already.",
            inline = False
        )

        # Bot Status
        help_status = discord.Embed(
            title = 'Bot Status',
            color = discord.Color.red()
        )
        help_status.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_status.add_field(
            name = 'Aliases',
            value = "`None`",
            inline = False
        )
        help_status.add_field(
            name = 'Usage',
            value = "`status`",
            inline = False,
        )
        help_status.add_field(
            name = 'Description',
            value = "Displays the bot's current version and other\ninformations.",
            inline = False
        )

        # Clear Message
        help_clear_message = discord.Embed(
            title = 'Clear Message',
            color = discord.Color.red()
        )
        help_clear_message.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_clear_message.add_field(
            name = 'Aliases',
            value = "`clrmsg`, `purge`",
            inline = False
        )
        help_clear_message.add_field(
            name = 'Usage',
            value = "`clear_message [amount max:100]`",
            inline = False,
        )
        help_clear_message.add_field(
            name = 'Description',
            value = "(Moderator)Clears the [amount] most recent messages in the channel.",
            inline = False
        )

        # Kick
        help_kick = discord.Embed(
            title = 'Kick',
            color = discord.Color.red()
        )
        help_kick.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_kick.add_field(
            name = 'Aliases',
            value = "None",
            inline = False
        )
        help_kick.add_field(
            name = 'Usage',
            value = "`kick <member> [reason]`",
            inline = False,
        )
        help_kick.add_field(
            name = 'Description',
            value = "(Moderator)Kicks the mentioned member, and logs the reason in Audit Log.",
            inline = False
        )

        # Ban
        help_ban = discord.Embed(
            title = 'Ban',
            color = discord.Color.red()
        )
        help_ban.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_ban.add_field(
            name = 'Aliases',
            value = "None",
            inline = False
        )
        help_ban.add_field(
            name = 'Usage',
            value = "`ban <member> [reason]`",
            inline = False,
        )
        help_ban.add_field(
            name = 'Description',
            value = "(Moderator)Bans the mentioned member, and logs the reason in Audit Log.",
            inline = False
        )

        # Say
        help_say = discord.Embed(
            title = 'Say',
            color = discord.Color.red()
        )
        help_say.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_say.add_field(
            name = 'Aliases',
            value = "None",
            inline = False
        )
        help_say.add_field(
            name = 'Usage',
            value = "`say <message>`",
            inline = False,
        )
        help_say.add_field(
            name = 'Description',
            value = "Repeats the said message.",
            inline = False
        )

        # 8ball
        help_8ball = discord.Embed(
            title = '8ball',
            color = discord.Color.red()
        )
        help_8ball.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_8ball.add_field(
            name = 'Aliases',
            value = "None",
            inline = False
        )
        help_8ball.add_field(
            name = 'Usage',
            value = "`8ball <question>`",
            inline = False,
        )
        help_8ball.add_field(
            name = 'Description',
            value = "Replies a Y/N to the question.",
            inline = False
        )

        # Throw
        help_throw = discord.Embed(
            title = 'Throw',
            color = discord.Color.red()
        )
        help_throw.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_throw.add_field(
            name = 'Aliases',
            value = "None",
            inline = False
        )
        help_throw.add_field(
            name = 'Usage',
            value = "`throw <member>`",
            inline = False,
        )
        help_throw.add_field(
            name = 'Description',
            value = "Throws something to the mentioned member.",
            inline = False
        )

        # Dice
        help_dice = discord.Embed(
            title = 'Dice',
            color = discord.Color.red()
        )
        help_dice.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_dice.add_field(
            name = 'Aliases',
            value = "`roll`",
            inline = False
        )
        help_dice.add_field(
            name = 'Usage',
            value = "`dice [face]`",
            inline = False,
        )
        help_dice.add_field(
            name = 'Description',
            value = "Rolls a [face] sided die.",
            inline = False
        )

        # Choose
        help_choose = discord.Embed(
            title = 'Choose',
            color = discord.Color.red()
        )
        help_choose.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_choose.add_field(
            name = 'Aliases',
            value = "None",
            inline = False
        )
        help_choose.add_field(
            name = 'Usage',
            value = "`choose <choices>`",
            inline = False,
        )
        help_choose.add_field(
            name = 'Description',
            value = "Chooses between <choices> that are separated by a comma(,).",
            inline = False
        )

        # Balance
        help_balance = discord.Embed(
            title = 'Balance',
            color = discord.Color.red()
        )
        help_balance.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_balance.add_field(
            name = 'Aliases',
            value = "`bal`",
            inline = False
        )
        help_balance.add_field(
            name = 'Usage',
            value = "`balance [member]`",
            inline = False,
        )
        help_balance.add_field(
            name = 'Description',
            value = "Shows how much money you have/member's money if mentioned.",
            inline = False
        )

        # Transfer
        help_transfer = discord.Embed(
            title = 'Transfer Money',
            color = discord.Color.red()
        )
        help_transfer.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_transfer.add_field(
            name = 'Aliases',
            value = "give",
            inline = False
        )
        help_transfer.add_field(
            name = 'Usage',
            value = "`transfer <member> <amount>`",
            inline = False,
        )
        help_transfer.add_field(
            name = 'Description',
            value = "Transfers <amount> of your money to the <member>.",
            inline = False
        )

        # Daily
        help_daily = discord.Embed(
            title = 'Daily',
            color = discord.Color.red()
        )
        help_daily.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_daily.add_field(
            name = 'Aliases',
            value = "None",
            inline = False
        )
        help_daily.add_field(
            name = 'Usage',
            value = "`daily`",
            inline = False,
        )
        help_daily.add_field(
            name = 'Description',
            value = "Gain money with a random amount depending on your level every 24 hours.",
            inline = False
        )

        # Action
        help_action = discord.Embed(
            title = 'Action/Fun Commands (1/2)',
            color = discord.Color.red()
        )
        help_action.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author,
        )
        help_action.add_field(
            name = 'Aliases',
            value = "Check the next page for a list of action commands."
        )
        help_action.add_field(
            name = 'Usage',
            value = '`<action> [member]`',
            inline = False
        )
        help_action.add_field(
            name = 'Description',
            value = "Temporarily Unavailable",
            inline = False
        )
        help_action2 = discord.Embed(
            title = 'Action/Fun Commands (2/2)',
            color = discord.Color.red()
        )
        help_action2.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_action2.add_field(
            name = 'Actions',
            value = 'Temporarily Unavailable',
            inline = False
        )

        # Work
        help_work = discord.Embed(
            title = 'work',
            color = discord.Color.red()
        )
        help_work.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_work.add_field(
            name = 'Aliases',
            value = 'None',
            inline = False
        )
        help_work.add_field(
            name = 'Usage',
            value = '`work`',
            inline = False
        )
        help_work.add_field(
            name = 'Description',
            value = "Get paid with a random amount depending on your level.\nCan be used twice every 6 hours.",
            inline = False
        )

        # Set Set Prefix
        help_setprefix = discord.Embed(
            title = 'Set Prefix',
            color = discord.Color.red()
        )
        help_setprefix.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_setprefix.add_field(
            name = 'Aliases',
            value = 'None',
            inline = False
        )
        help_setprefix.add_field(
            name = 'Usage',
            value = '`setprefix <prefix>`',
            inline = False
        )
        help_setprefix.add_field(
            name = 'Description',
            value = "(Admin)Changes the prefix for your server.",
            inline = False
        )

        # Reputation
        help_reputation = discord.Embed(
            title = 'Reputation',
            color = discord.Color.red()
        )
        help_reputation.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_reputation.add_field(
            name = 'Aliases',
            value = "`rep`",
            inline = False
        )
        help_reputation.add_field(
            name = 'Usage',
            value = "`reputation <member>`",
            inline = False
        )
        help_reputation.add_field(
            name = 'Description',
            value = "Gives <member> a reputation point. Can only be used once per day.",
            inline = False
        )

        # Profile
        help_profile = discord.Embed(
            title = 'Profile',
            color = discord.Color.red()
        )
        help_profile.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_profile.add_field(
            name = 'Aliases',
            value = '`pr`',
            inline = False
        )
        help_profile.add_field(
            name = 'Usage',
            value = "`profile [member]`",
            inline = False
        )
        help_profile.add_field(
            name = 'Description',
            value = "Shows your profile card/[member]'s profile card if specified.",
            inline = False
        )

        # Inventory
        help_inventory = discord.Embed(
            title = 'Inventory',
            color = discord.Color.red()
        )
        help_inventory.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_inventory.add_field(
            name = 'Aliases',
            value = '`inv`',
            inline = False
        )
        help_inventory.add_field(
            name = 'Usage',
            value = "`inventory [member]`",
            inline = False
        )
        help_inventory.add_field(
            name = 'Description',
            value = "Shows your inventory/[member]'s inventory if specified.",
            inline = False
        )

        # Bookshelf
        help_bookshelf = discord.Embed(
            title = 'Bookshelf',
            color = discord.Color.red()
        )
        help_bookshelf.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_bookshelf.add_field(
            name = 'Aliases',
            value = '`books`',
            inline = False
        )
        help_bookshelf.add_field(
            name = 'Usage',
            value = "`bookshelf [member]`",
            inline = False
        )
        help_bookshelf.add_field(
            name = 'Description',
            value = "Shows your bookshelf contents/[member]'s bookshelf contents if specified.",
            inline = False
        )

        # Read
        help_read = discord.Embed(
            title = 'Read',
            color = discord.Color.red()
        )
        help_read.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_read.add_field(
            name = 'Aliases',
            value = '`books`',
            inline = False
        )
        help_read.add_field(
            name = 'Usage',
            value = "`read <book>`",
            inline = False
        )
        help_read.add_field(
            name = 'Description',
            value = "Reads <book>. Can only be used twice every hour.",
            inline = False
        )

        # Support
        help_support = discord.Embed(
            title = 'Support',
            color = discord.Color.red()
        )
        help_support.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_support.add_field(
            name = 'Aliases',
            value = 'None',
            inline = False
        )
        help_support.add_field(
            name = 'Usage',
            value = "`support`",
            inline = False
        )
        help_support.add_field(
            name = 'Description',
            value = "A link for the support ~~server~~ Guild.",
            inline = False
        )

        # Guild House
        help_train = discord.Embed(
            title = 'Training',
            color = discord.Color.red()
        )
        help_train.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_train.add_field(
            name = 'Aliases',
            value = 'None',
            inline = False
        )
        help_train.add_field(
            name = 'Usage',
            value = "`train`",
            inline = False
        )
        help_train.add_field(
            name = 'Description',
            value = "Train to gain exps.\nCan only be used once every 3 hours.",
            inline = False
        )

        # Commission
        help_commission = discord.Embed(
            title = 'Commissions (1/2)',
            color = discord.Color.red()
        )
        help_commission.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_commission.add_field(
            name = 'Aliases',
            value = 'None',
            inline = False
        )
        help_commission.add_field(
            name = 'Usage',
            value = "`commission <type>`",
            inline = False
        )
        help_commission.add_field(
            name = 'Description',
            value = "Different task that gives reward depending on the <type> specified.\nCan only be used once daily.",
            inline = False
        )
        help_commission2 = discord.Embed(
            title = 'Commissions (2/2)',
            color = discord.Color.red()
        )
        help_commission2.set_footer(
            icon_url = ctx.author.avatar_url,
            text = ctx.author
        )
        help_commission2.add_field(
            name = 'Actions',
            value = '`exp`, `credits`',
            inline = False
        )
    ###########################################################################
    ###########################################################################

        if page is None:
            await ctx.send(embed = help)

        elif page == 'ping':
            await ctx.send(embed = help_ping)

        elif page == 'status':
            await ctx.send(embed = help_status)

        elif page == 'clear_message':
            await ctx.send(embed = help_clear_message)

        elif page == 'kick':
            await ctx.send(embed = help_kick)

        elif page == 'ban':
            await ctx.send(embed = help_ban)

        elif page == 'say':
            await ctx.send(embed = help_say)

        elif page == '8ball':
            await ctx.send(embed = help_8ball)

        elif page == 'throw':
            await ctx.send(embed = help_throw)

        elif page == 'dice':
            await ctx.send(embed = help_dice)

        elif page == 'choose':
            await ctx.send(embed = help_choose)

        elif page == 'balance':
            await ctx.send(embed = help_balance)

        elif page == 'transfer':
            await ctx.send(embed = help_transfer)

        elif page == 'daily':
            await ctx.send(embed = help_daily)

        elif page == 'action' or page == 'fun':
            msg_help = await ctx.send(embed = help_action)

            await msg_help.add_reaction('\u25c0')
            await msg_help.add_reaction('\u25b6')

            def check(reaction, user):
                return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id and \
                        str(reaction.emoji) in ['\u25c0', '\u25b6']

            while True:
                try:
                    reaction, user = await self.client.wait_for('reaction_add', check = check, timeout = 30)
                except asyncio.TimeoutError:
                    await msg_help.clear_reactions()
                    break

                else:
                    if str(reaction.emoji) == '\u25c0':
                        await msg_help.remove_reaction(reaction, user)
                        await msg_help.edit(embed = help_action)
                        continue
                    if str(reaction.emoji) == '\u25b6':
                        await msg_help.remove_reaction(reaction, user)
                        await msg_help.edit(embed = help_action2)
                        continue

        elif page == 'work':
            await ctx.send(embed = help_work)

        elif page == 'setprefix':
            await ctx.send(embed = help_setprefix)

        elif page == 'reputation' or page == 'rep':
            await ctx.send(embed = help_reputation)

        elif page == 'profile' or page == 'pr':
            await ctx.send(embed = help_profile)

        elif page == 'inventory' or page == 'inv':
            await ctx.send(embed = help_inventory)

        elif page == 'bookshelf' or page == 'books':
            await ctx.send(embed = help_bookshelf)

        elif page == 'read':
            await ctx.send(embed = help_read)

        elif page == 'support':
            await ctx.send(embed = help_support)

        elif page == 'train':
            await ctx.send(embed = help_train)

        elif page == 'commission':
            msg_help = await ctx.send(embed = help_commission)

            await msg_help.add_reaction('\u25c0')
            await msg_help.add_reaction('\u25b6')

            def check(reaction, user):
                return user.id == ctx.author.id and reaction.message.channel.id == ctx.channel.id and \
                        str(reaction.emoji) in ['\u25c0', '\u25b6']

            while True:
                try:
                    reaction, user = await self.client.wait_for('reaction_add', check = check, timeout = 30)
                except asyncio.TimeoutError:
                    await msg_help.clear_reactions()
                    break

                else:
                    if str(reaction.emoji) == '\u25c0':
                        await msg_help.remove_reaction(reaction, user)
                        await msg_help.edit(embed = help_commission)
                        continue
                    if str(reaction.emoji) == '\u25b6':
                        await msg_help.remove_reaction(reaction, user)
                        await msg_help.edit(embed = help_commission2)
                        continue

        else:
            await ctx.send("Sorry, It seems that the command you are trying to look for doesn't exist.")

    ###########################################################################
    ###########################################################################

    @commands.command()
    async def support(self, ctx):
        await ctx.send("**Join the support server:**")
        await ctx.send('https://discord.gg/KzEsU7q')

def setup(client):
    client.add_cog(Help(client))
