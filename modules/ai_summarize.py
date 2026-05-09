import os
from groq import Groq
from dotenv import load_dotenv

# .env file se Groq API key load karna
load_dotenv()
GROQ_KEY = os.getenv('GROQ_API_KEY')

def generate_summary(raw_text):
    """
    Groq AI (Llama 3.1) se English summary banwane ke liye updated function with Fallback.
    """
    print("Generating script via Groq AI (Llama 3.1)...")
    
    if not GROQ_KEY:
        return "Groq API key missing."

    try:
        client = Groq(api_key=GROQ_KEY)
        
        # Naya aur zyada smart English Prompt
        prompt = f"""
        You are a professional and engaging podcast host. 
        Create a short (1-2 minute) conversational script in ENGLISH about the topic.
        The script should sound very natural and energetic.
        Start the script directly (e.g., "Hello everyone, let's dive into...").
        Do not use any Urdu words. Focus only on the most important points.
        
        Raw Data from internet:
        {raw_text}
        
        IMPORTANT INSTRUCTION: If the Raw Data says no information was found (for example: "koi naya data nahi mila"), DO NOT say there are no updates or apologize. Instead, use your own internal AI knowledge to discuss the latest general trends, facts, or give an interesting overview of the topic.
        """
        
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
        )
        
        return chat_completion.choices[0].message.content
        
    except Exception as e:
        print(f"AI Summary Error: {e}")
        return "Sorry, I am unable to generate the summary at the moment."
    """
    Groq AI (Llama 3.1) se English summary banwane ke liye updated function.
    """
    print("Groq AI (Llama 3.1) se English summary banwayi ja rahi hai...")
    
    if not GROQ_KEY:
        return "Groq API key missing."

    try:
        client = Groq(api_key=GROQ_KEY)
        
        # English Prompt taake AI English mein hi script likhay
        prompt = f"""
        You are a professional and engaging podcast host. 
        Read the following news updates and create a short (1-2 minute) conversational script in ENGLISH.
        The script should sound very natural and energetic.
        Start the script directly (e.g., "Hello everyone, here are today's top updates...").
        Do not use any Urdu words. Focus only on the most important points.
        If no data is found, simply say that there are no major updates for this topic today.
        
        Raw Data:
        {raw_text}
        """
        
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
        )
        
        return chat_completion.choices[0].message.content
        
    except Exception as e:
        print(f"AI Summary Error: {e}")
        return "Sorry, I am unable to generate the summary at the moment."
# Testing Block
if __name__ == "__main__":
    test_data = "News 1: AI is growing fast. News 2: Python is the best language."
    print(generate_summary(test_data))