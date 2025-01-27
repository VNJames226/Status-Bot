import discord
from discord.ext import commands, tasks
import asyncio
from mcstatus import JavaServer, MinecraftServer
from datetime import datetime
import re
# Bot-Setup
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Bot-Konfiguration
BOT_TOKEN = "bot_token"  # Hier deinen Bot-Token einfügen
MINECRAFT_SERVER_IP = "Mc_Server_ip"  # Hier deine Minecraft-Server-IP
STATUS_CHANNEL_ID = 38745386535  # <--- Hier bitte deine Status Channel id einfügen
MESSAGE_ID = None
VOIDBEST_STATUS_LINK = "status_seite"  # Hier den Link zur Status Seite einfügen

# Farben für das Embed
ONLINE_COLOR = 0x2ecc71    # Grün
OFFLINE_COLOR = 0xe74c3c   # Rot


async def get_minecraft_status():
    """Holt den Status des Minecraft-Servers"""
    try:
        server = JavaServer.lookup(MINECRAFT_SERVER_IP)
        status = await server.async_status()
        player_list = []
        if hasattr(status, 'players') and hasattr(status.players, 'sample') and status.players.sample:
            player_list = [player.name for player in status.players.sample]
        return {
            "online": True,
            "players": f"{status.players.online}/{status.players.max}",
            "ping": f"{status.latency:.1f}ms",
            "player_list": player_list,
            "version": status.version.name
        }
    except:
        return {
            "online": False,
            "players": "0/0",
            "ping": "N/A",
            "player_list": [],
            "version": "Unbekannt"
        }


def get_moderators(server):
    """Holt die Moderatoren des Minecraft-Servers"""
    try:
        status = server.status()
        player_list = []
        if hasattr(status, 'players') and hasattr(status.players, 'sample') and status.players.sample:
            player_list = [player.name for player in status.players.sample]
        return [player for player in player_list if re.match(r'^(?:[A-Za-z0-9_]){3,16}$', player)]
    except:
        return []


def get_minecraft_motd(server):
    """Holt die MOTD des Minecraft-Servers"""
    try:
        server = MinecraftServer.lookup(server)
        status = server.status()
        return status.description['text']
    except:
        return "N/A"


@tasks.loop(seconds=1)
async def update_status_message():
    global MESSAGE_ID
    channel = bot.get_channel(STATUS_CHANNEL_ID)
    if not channel:
        return

    # Discord-Status abrufen
    guild = channel.guild
    online_members = len([m for m in guild.members if m.status != discord.Status.offline])
    bots = len([m for m in guild.members if m.bot])
    humans = guild.member_count - bots

    # Minecraft-Status abrufen
    mc_status = await get_minecraft_status()

    # Moderatoren abrufen
    server = JavaServer.lookup(MINECRAFT_SERVER_IP)
    moderators = get_moderators(server)

    # Embed erstellen
    embed = discord.Embed(
        title="🎮 Server Status",
        description="Echtzeit-Status unserer Server",
        color=ONLINE_COLOR if mc_status["online"] else OFFLINE_COLOR,
        timestamp=datetime.now()
    )

    # Discord Server Status
    discord_status = (
        f"👥 Gesamt Mitglieder: **{guild.member_count}**\n"
        f"🟢 Online: **{online_members}**\n"
        f"🤖 Bots: **{bots}**\n"
        f"👤 Menschen: **{humans}**\n"
        f"💎 Server Boosts: **{guild.premium_subscription_count}**\n"
        f"📊 Boost Level: **{guild.premium_tier}**"
    )
    embed.add_field(
        name="🔷 Discord Server",
        value=discord_status,
        inline=False
    )

    # Minecraft Server Status
    mc_status_text = (
        f"⚡ Status: **{'🟢 Online' if mc_status['online'] else '🔴 Offline'}**\n"
        f"👥 Spieler: **{mc_status['players']}**\n"
        f"📶 Ping: **{mc_status['ping']}**\n"
        f"🔧 Version: **{mc_status['version']}**"
    )

    # Füge Spielerliste hinzu, wenn Spieler online sind
    if mc_status['player_list']:
        mc_status_text += "\n\n**Online Spieler:**\n" + "\n".join(f"• {player}" for player in mc_status['player_list'])

    # Füge Moderatoren hinzu, wenn welche vorhanden sind
    if moderators:
        mc_status_text += "\n\n**Moderatoren:**\n" + "\n".join(f"• {moderator}" for moderator in moderators)

    embed.add_field(
        name="⛏️ Minecraft Server",
        value=mc_status_text,
        inline=False
    )

    # Server IP hinzufügen
    embed.add_field(
        name="🌐 Server IP",
        value=f"```{MINECRAFT_SERVER_IP}```",
        inline=False
    )

    # Voidbest.net Status-Link hinzufügen
    embed.add_field(
        name="🌐 Status Seite",
        value=f"[Hier klicken]({VOIDBEST_STATUS_LINK})",
        inline=False
    )

    # Footer und Thumbnail
    embed.set_footer(text="Zuletzt aktualisiert • Bot by dein Name")  # hier dein Name einfügen
    embed.set_thumbnail(url="https://dein.logo.hier.rein")  # Füge hier dein Server-Icon ein

    try:
        if MESSAGE_ID is None:
            message = await channel.send(embed=embed)
            MESSAGE_ID = message.id
        else:
            message = await channel.fetch_message(MESSAGE_ID)
            await message.edit(embed=embed)
    except discord.NotFound:
        message = await channel.send(embed=embed)
        MESSAGE_ID = message.id
    except Exception as e:
        print(f"Fehler beim Aktualisieren der Status-Nachricht: {e}")


@bot.event
async def on_ready():
    print(f'{bot.user} is ready and connected to Discord!')
    update_status_message.start()


@bot.event
async def on_member_join(member):
    await update_status_message()


@bot.event
async def on_member_remove(member):
    await update_status_message()


@bot.event
async def on_member_update(before, after):
    if before.status != after.status:
        await update_status_message()


@bot.event
async def on_guild_update(before, after):
    await update_status_message()


# Starte den Bot
bot.run(BOT_TOKEN)




