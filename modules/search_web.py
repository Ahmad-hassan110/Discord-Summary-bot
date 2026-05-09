import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import quote

def get_search_results(topic, max_results=5):
    """
    Yeh function Google News RSS Feed use karta hai jo 100% free aur stable hai.
    """
    print(f"Google News par search ho raha hai: {topic}...")
    
    try:
        # Topic ko URL format mein convert karna (e.g., "AI news" -> "AI%20news")
        safe_topic = quote(topic)
        url = f"https://news.google.com/rss/search?q={safe_topic}&hl=en-US&gl=US&ceid=US:en"
        
        # Request bhejna (User-Agent add kiya hai taake block na ho)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        response = urllib.request.urlopen(req)
        xml_data = response.read()
        
        # XML (RSS) data ko parhna
        root = ET.fromstring(xml_data)
        
        combined_text = f"--- Topic: {topic} ---\n\n"
        
        # RSS mein har news ek <item> tag ke andar hoti hai
        items = root.findall('.//item')
        
        if not items:
            return f"Mujhe '{topic}' ke bare mein koi naya data nahi mila."

        # Top 5 news titles aur unki date nikalna
        for index, item in enumerate(items[:max_results], 1):
            title = item.find('title').text
            date = item.find('pubDate').text
            
            combined_text += f"News {index}:\n"
            combined_text += f"Title: {title}\n"
            combined_text += f"Date: {date}\n\n"
            
        return combined_text
        
    except Exception as e:
        print(f"Error aagaya search karte hue: {e}")
        return f"Mujhe '{topic}' ke bare mein information nikalte hue error aagaya."

# Testing Block
if __name__ == "__main__":
    test_topic = "Artificial Intelligence latest trends"
    print("Testing Search Module...\n")
    output = get_search_results(test_topic)
    print(output)