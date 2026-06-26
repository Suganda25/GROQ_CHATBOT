import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)
print("************************************")
print("AI Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Good bye!")       
        break

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )
        bot_reply = response.choices[0].message.content
        print("Bot:", bot_reply)
        print("************************************")

    except Exception as e:
        print("Error:", e)