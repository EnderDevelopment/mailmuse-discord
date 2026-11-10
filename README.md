# Discord Email Draft Bot

MailMuse is a Python Discord bot for generating email drafts with the `/email` slash command. It creates drafts locally without an AI provider or email-sending integration, and replies privately to the user who requested them.

## Install

1. Create a Discord application and bot in the Discord Developer Portal.
2. Invite the bot to your server with the `bot` and `applications.commands` scopes, and grant it permission to use application commands and send messages.
3. Install Python 3.10 or newer.
4. Install the dependencies:
   ```sh
   python -m pip install -r requirements.txt
   ```
5. Set `DISCORD_TOKEN` to your bot token in the environment or in a `.env` file based on `.env.example`. Keep the token private.
6. Start the bot:
   ```sh
   python main.py
   ```

## Use

1. In Discord, run `/email`.
2. Enter the email purpose and choose a tone: professional, friendly, formal, casual, or persuasive.
3. Optionally enter a recipient and details to include.
4. Review the private draft, including its suggested subject, and replace `[Your name]` before sending it yourself.

The purpose must be no more than 500 characters, the recipient no more than 80 characters, and the details no more than 700 characters.

---

More Discord bot projects by EnderDevelopment: https://github.com/EnderDevelopment

Project page: https://dash.enderdevelopment.com/community/c52438a9-f96f-42c1-bd03-b14bdb196b18?utm_source=github&utm_medium=readme&utm_campaign=auto_publish&utm_content=c52438a9-f96f-42c1-bd03-b14bdb196b18
