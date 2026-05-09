import edge_tts
import asyncio
import os

OUTPUT_DIR = "temp_audio"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "daily_summary.mp3")

async def generate_audio(text):
    """
    Yeh function text ko speech (mp3) mein convert karega using Microsoft Edge TTS.
    """
    print("Converting text to speech (Audio generation in progress)...")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    voice = "en-US-ChristopherNeural" 
    
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(OUTPUT_FILE)
        
        print(f"Audio successfully generated: {OUTPUT_FILE}")
        return OUTPUT_FILE
        
    except Exception as e:
        print(f"Error occurred while generating audio: {e}")
        return None

# Testing Block
if __name__ == "__main__":
    test_text = "Hello Ahmed! This is a test audio for your AI Daily Summary Bot. The system is working perfectly."
    print("Testing TTS Module...\n")
    
    asyncio.run(generate_audio(test_text))