import discord
import requests

TOKEN = "YOUR_DISCORD_BOT_TOKEN"

WEBHOOK_URL = "YOUR_N8N_WEBHOOK_URL"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):

    print(f"MESSAGE RECEIVED: {message.author} - {message.content}")

    if message.author == client.user:
        return

    # Test command
    if message.content.lower() == "hello":
        await message.channel.send("Hello! I am alive.")
        return

    # Email command
    if message.content.startswith("sendmail "):

        parts = message.content.split(" ", 2)

        if len(parts) < 3:
            await message.channel.send(
                "Usage:\nsendmail recipient@example.com Your Topic Here"
            )
            return

        recipient = parts[1]
        topic = parts[2]

        data = {
            "recipient": recipient,
            "topic": topic
        }

        try:
            response = requests.post(
                WEBHOOK_URL,
                json=data
            )

            print("Status Code:", response.status_code)
            print("Response:", response.text)

            await message.channel.send(
                f"Request sent!\nRecipient: {recipient}\nTopic: {topic}"
            )

        except Exception as e:
            print("ERROR:", e)

            await message.channel.send(
                f"Error sending request:\n{e}"
            )


client.run(TOKEN)