from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("OPENROUTER_API_KEY")

if key:
    print(" .env loaded successfully.")
    print("Key starts with:", key[:7])
else:
    print(" .env not loaded.")