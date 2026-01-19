<div align="center">
</div>

# Discord Status Bot (Python)

Ein leistungsstarker Bot zur Überwachung deines Minecraft-Servers direkt in Discord. Die Informationen werden sofort in einem professionellen Embed aktualisiert.

## ✨ Funktionen

### 🎮 Minecraft Server Status
* **Server Status:** Live-Anzeige, ob der Server online oder offline ist.
* **Spieleranzahl:** Aktuelle sowie maximale Spieleranzahl auf einen Blick.
* **Version:** Information zur derzeitigen Server-Version.

### ℹ️ Server-Informationen & Updates
* **IP-Adresse:** Zeigt die IP-Adresse des Servers im Embed an.
* **Status-Seite Verlinkung:** Direktlink zu einer detaillierten Status-Seite.
* **Auto-Update:** Automatische Aktualisierung der Informationen alle **30 Sekunden**.
* **Benutzerdefinierte Bot-Signatur:** Zeigt den genauen Zeitpunkt der letzten Aktualisierung an.

---

## 🚀 Schnellstart

**Voraussetzungen:** Python 3.8+ sowie die Bibliotheken `discord.py` und `mcstatus`.

1. **Abhängigkeiten installieren:**
   `pip install discord.py mcstatus python-dotenv`

2. **Konfiguration:**
   Erstelle eine `.env` Datei im Hauptverzeichnis:
   ```env
   TOKEN=DEIN_DISCORD_BOT_TOKEN
   MC_SERVER_IP=play.deinserver.de
   CHANNEL_ID=123456789012345678
