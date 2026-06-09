# AI Daily Summary Agent 

An intelligent Discord bot (AI Agent) that fetches the latest news on user-specified topics, generates a concise, conversational summary using Meta's Llama 3.1, and delivers it as a professional audio podcast directly in your Discord server.

## Features
* **Smart Information Retrieval:** Fetches real-time data using Google News based on user topics.
* **AI-Powered Summarization:** Utilizes **Groq API (Llama-3.1-8b-instant)** to craft highly engaging, podcast-style scripts in English.
* **Intelligent Fallback:** If no breaking news is found, the AI seamlessly pivots to discussing general trends and insights about the topic using its internal knowledge base.
* **Text-to-Speech (TTS):** Converts the AI script into high-quality human-like audio using Microsoft Edge TTS.
* **Interactive Commands:** Manage your topic queue effortlessly through simple Discord commands.

## Tech Stack
* **Language:** Python 3.x
* **AI Engine:** Groq API (Meta Llama 3.1)
* **Voice Synthesis:** Edge-TTS
* **Discord API:** `discord.py`

## Prerequisites
Before running this bot, ensure you have the following installed:
* [Python 3.8+](https://www.python.org/downloads/)
* A Discord Bot Token (from the [Discord Developer Portal](https://discord.com/developers/applications))
* A free Groq API Key (from [Groq Console](https://console.groq.com/))

## Installation & Setup

**1. Clone the repository:**
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
Install required dependencies:
pip install -r requirements.txt
Configure Environment Variables:
DISCORD_TOKEN=your_discord_bot_token_here
GROQ_API_KEY=your_groq_api_key_here
