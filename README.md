<div align="center">
</div>

# Discord Status Bot (Python)

Ein leistungsstarker Bot zur Überwachung deines Discord-Servers und deines Minecraft-Servers. Die Informationen werden alle 30 Sekunden in einem professionellen Embed aktualisiert.

## ✨ Funktionen

### 📊 Discord Server Status
* **Mitgliederübersicht:** Anzeige der Gesamtzahl, Online-Mitglieder, Menschen vs. Bots.
* **Server Boosts:** Aktuelle Anzahl der Boosts und das erreichte Server-Level.

### 🎮 Minecraft Server Status
* **Server Status:** Live-Anzeige, ob der Server online oder offline ist.
* **Spieleranzahl:** Aktuelle und maximale Spieleranzahl auf einen Blick.
* **Details:** Anzeige von Server-Ping und der installierten Version.

### ℹ️ Server-Informationen & Updates
* **IP-Adresse:** Schneller Zugriff auf die Server-Adresse.
* **Verlinkung:** Direktlink zur detaillierten Status-Seite.
* **Auto-Update:** Automatische Aktualisierung alle **30 Sekunden**.
* **Zeitstempel:** Benutzerdefinierte Signatur mit der letzten Aktualisierungszeit.

---

## 🚀 Schnellstart

**Voraussetzungen:** Python 3.8+ sowie die Bibliotheken `discord.py` und `mcstatus`.

1. **Abhängigkeiten installieren:**
   `pip install discord.py mcstatus python-dotenv`

2. **Konfiguration:**
   Erstelle eine `.env` Datei und hinterlege dort deinen Token und die Server-IP:
   ```env
   TOKEN=DEIN_BOT_TOKEN
   GUILD_ID=DEIN_SERVER_ID
   MC_SERVER_IP=play.deinserver.de
   CHANNEL_ID=1234567890
