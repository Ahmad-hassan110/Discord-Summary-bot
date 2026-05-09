import discord
from discord.ext import commands
import json
import os
import asyncio

# Apne banaye hue modules import kar rahe hain
from modules.search_web import get_search_results
from modules.ai_summarize import generate_summary
from modules.tts_generator import generate_audio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

DATA_FILE = 'data/saved_topics.json'

def load_topics():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_topics(topics):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(topics, f, indent=4)

@bot.event
async def on_ready():
    print(f'System Ready: {bot.user} is live on Discord!')

@bot.command()
async def add(ctx, *, topic: str):
    topics = load_topics()
    topics.append(topic)
    save_topics(topics)
    await ctx.send(f'✅ Topic added: **{topic}**')

@bot.command()
async def topics(ctx):
    topics = load_topics()
    if not topics:
        await ctx.send("📭 No topics added yet.")
    else:
        response = "📝 **Today's Topics:**\n"
        for index, topic in enumerate(topics, 1):
            response += f"{index}. {topic}\n"
        await ctx.send(response)

@bot.command()
async def get_summary(ctx):
    topics = load_topics()
    if not topics:
        await ctx.send("📭 No topics added yet. Please add topics using `!add` command.")
        return
    
    await ctx.send("⚙️ Generating summaries for today's topics. Please wait...")
    
    for topic in topics:
        await ctx.send(f"🔍 Processing: **{topic}**...")
        
        # Step 1: Web Search
        raw_data = get_search_results(topic)
        
        # Step 2: AI Summarize
        script = generate_summary(raw_data)
        
        # Step 3: Text-to-Speech (Audio Generation)
        audio_path = await generate_audio(script)
        
        # Step 4: Discord par Audio File send karna
        if audio_path and os.path.exists(audio_path):

            await ctx.send(f"🎙️ **Voice Summary for:** {topic}", file=discord.File(audio_path))
            
            os.remove(audio_path)
        else:
            await ctx.send(f"❌ '{topic}' problem in audio generation.\n\n{script}")
            
    save_topics([])
    await ctx.send("✅ All summaries generated and topics list cleared for tomorrow!")