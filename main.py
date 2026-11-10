import os
import re
from textwrap import dedent

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

TONE_GUIDANCE = {
    "professional": "Use a clear, polished, business-appropriate voice.",
    "friendly": "Use a warm, approachable voice while staying considerate.",
    "formal": "Use a respectful, formal voice and complete sentences.",
    "casual": "Use a natural, relaxed voice without sounding careless.",
    "persuasive": "Use a confident, respectful voice focused on the requested outcome.",
}


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def generate_email(purpose: str, recipient: str, tone: str, details: str | None) -> tuple[str, str]:
    purpose = clean(purpose)
    recipient = clean(recipient)
    details = clean(details or "")

    subject = purpose.rstrip(".!? ")
    if len(subject) > 72:
        subject = subject[:69].rstrip() + "..."
    subject = subject[:1].upper() + subject[1:]

    greeting = f"Hello {recipient}," if recipient else "Hello,"
    detail_paragraph = f"\n\n{details}" if details else ""
    instruction = TONE_GUIDANCE[tone]

    if tone == "casual":
        close = "Thanks,\n[Your name]"
    elif tone == "friendly":
        close = "Best,\n[Your name]"
    elif tone == "formal":
        close = "Sincerely,\n[Your name]"
    else:
        close = "Kind regards,\n[Your name]"

    body = dedent(f"""\
        {greeting}

        I'm writing to {purpose.rstrip('.!? ')}.{detail_paragraph}

        Please let me know what you think or if you need any further information.

        {close}
    """).strip()

    # Keep the requested tone explicit in the generation policy and avoid returning empty drafts.
    if not instruction or not body:
        raise ValueError("Unable to generate an email draft.")
    return subject, body


class EmailBot(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        await self.tree.sync()


client = EmailBot()


@client.tree.command(name="email", description="Generate an email draft")
@app_commands.describe(
    purpose="What the email should accomplish",
    recipient="Who the email is addressed to (optional)",
    tone="Choose the writing tone",
    details="Optional facts or context to include",
)
@app_commands.choices(tone=[
    app_commands.Choice(name="Professional", value="professional"),
    app_commands.Choice(name="Friendly", value="friendly"),
    app_commands.Choice(name="Formal", value="formal"),
    app_commands.Choice(name="Casual", value="casual"),
    app_commands.Choice(name="Persuasive", value="persuasive"),
])
async def email_command(
    interaction: discord.Interaction,
    purpose: str,
    tone: app_commands.Choice[str],
    recipient: str | None = None,
    details: str | None = None,
) -> None:
    if len(purpose) > 500 or (recipient and len(recipient) > 80) or (details and len(details) > 700):
        await interaction.response.send_message(
            "Please keep purpose under 500 characters, recipient under 80, and details under 700.",
            ephemeral=True,
        )
        return

    subject, body = generate_email(purpose, recipient or "", tone.value, details)
    result = f"**Subject:** {subject}\n\n{body}"
    await interaction.response.send_message(result, ephemeral=True)


if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("Set DISCORD_TOKEN in your environment or .env file.")
    client.run(TOKEN)
