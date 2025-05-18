import os
import logging
import json
from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionMessageParam  # Assuming this is available for chat use
import sys

# Load environment variables from the .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Define the messages you want to send in a conversation (example)
shoe_conversation = [
    "SalesBot: Hi, I'm Allbirds Assistant! How can I help you today?",
    "John: Hi, I'm looking for a new pair of shoes.",
    "SalesBot: Of course! What kind of material are you looking for?",
    "John: I'm looking for shoes made out of wool",
    "SalesBot: We have just what you are looking for, how do you like our Men's SuperLight Wool Runners - Dark Grey (Medium Grey Sole)? They use the SuperLight Foam technology.",
    "John: Oh, actually I bought those 2 months ago, but unfortunately found out that I was allergic to wool. I think I will pass on those, maybe there is something with a retro look that you could suggest?",
    "SalesBot: I'm sorry to hear that! Would you be interested in Men's Couriers - (Blizzard Sole) model? We have them in Natural Black and Basin Blue colors",
    "John: Oh that is perfect, I LOVE the Natural Black color! I will take those."
]

# Define a method to add the conversation as messages using Groq
def add_messages(client: Groq):
    msgs = []
    for message in shoe_conversation:
        if "SalesBot" in message:
            role = "system"  # Assuming SalesBot messages are from the system
        else:
            role = "user"  # Assuming user messages are from the user
        msgs.append({'role': role, 'content': message})

    try:
        # Make a chat completion request to the Groq client (synchronous version)
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",  # Example model, adjust as needed
            messages=msgs,
            max_tokens=2048,
            temperature=0.7
        )
        
        # Extract the response content (adjust based on actual response format)
        response_content = response.choices[0].message.content if hasattr(response, 'choices') else 'No content'
        
        # Print or process the response content as a serializable object
        print(f"Response from Groq: {response_content}")
        
        # Optionally, serialize this content to JSON if needed
        serialized_response = json.dumps({'response': response_content}, indent=2)
        print(serialized_response)

    except Exception as e:
        logger.error(f"Error adding messages: {e}")

# Main function
if __name__ == "__main__":
    add_messages(client)
