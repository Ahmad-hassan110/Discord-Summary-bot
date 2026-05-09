import edge_tts
import asyncio
import os

# Output folder aur file ka naam set kar rahe hain
OUTPUT_DIR = "temp_audio"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "daily_summary.mp3")

async def generate_audio(text):
    """
    Yeh function text ko speech (mp3) mein convert karega using Microsoft Edge TTS.
    """
    print("Voice note banaya ja raha hai...")
    
    # Agar temp_audio folder nahi hai toh bana lo
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    voice = "en-US-ChristopherNeural" 
    
    try:
        # Communicate object banana aur file save karna
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(OUTPUT_FILE)
        
        print(f"Audio successfully save ho gayi: {OUTPUT_FILE}")
        return OUTPUT_FILE
        
    except Exception as e:
        print(f"Audio generation mein error aaya: {e}")
        return None

# Testing Block
if __name__ == "__main__":
    test_text = "Hello Ahmed! This is a test audio for your AI Daily Summary Bot. The system is working perfectly."
    print("Testing TTS Module...\n")
    
    # Kyunke edge-tts asynchronous (async) library hai, hume asyncio.run() use karna parta hai
    asyncio.run(generate_audio(test_text))