# Discord Email Draft Bot

MailMuse is a Discord email draft bot that turns a stated purpose, optional recipient, chosen tone, and extra details into a ready-to-edit email draft. It uses a built-in template and does not require an AI provider or send emails.

## Install

1. Install Python 3.10 or newer.
2. Install the dependencies with `python -m pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and set `DISCORD_TOKEN` to your Discord bot token.
4. In the Discord Developer Portal, create an application and bot. Invite it to your server with the `bot` and `applications.commands` scopes and permission to use application commands and send messages.
5. Start the bot with `python main.py`. Slash commands sync at startup; `/email` may take a short time to appear.

## Use

1. Run `/email` in a server where the bot is installed.
2. Enter the email purpose and select a tone: professional, friendly, formal, casual, or persuasive. Optionally provide a recipient and details.
3. Review the private draft returned by the bot. Replace `[Your name]` and make any needed edits before sending it yourself.

---

More Discord bot projects by EnderDevelopment: https://github.com/EnderDevelopment

Project page: https://dash.enderdevelopment.com/community/c52438a9-f96f-42c1-bd03-b14bdb196b18?utm_source=github&utm_medium=readme&utm_campaign=auto_publish&utm_content=c52438a9-f96f-42c1-bd03-b14bdb196b18
