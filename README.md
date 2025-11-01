
🧠 README.md

# 🧩 AI Prompt Task — Moderated Chat using OpenRouter API

A simple Python project that demonstrates:
- Sending user prompts to an AI model (via *OpenRouter API*)
- Using a *system prompt* to guide model behavior
- Implementing *input & output moderation*
- Loading API keys securely from a .env file
- Writing clean, modular code with separation of concerns

---

## ⚙ Features

✅ Collects *user prompts* dynamically  
✅ Uses a *system prompt* to define AI personality  
✅ Performs *moderation checks* on both input and output  
✅ *Redacts* unsafe responses automatically  
✅ Uses *OpenRouter API* (free-tier supported)  
✅ Loops for *continuous chat* until the user exits  
✅ Organized into multiple files for clarity and maintainability


## 🧩 Requirements

- Python *3.8+*
- Dependencies:
  ```bash
  pip install requests python-dotenv


---

🔐 Environment Setup

Create a .env file in your project root and add your OpenRouter API key:

OPENROUTER_API_KEY=sk-or-v1-your-openrouter-key

> ⚠ Never share or commit your API key publicly.



If you don’t have one yet, get a free key from
🔗 https://openrouter.ai/keys


---

🚀 Running the App

Run this command in your terminal:

python main.py

You’ll see:

🤖 Chat started! Type 'exit' to quit.

You: hi
AI: Hello there! How are you doing today?

Keep chatting until you type exit or quit to end the session.


---

🛡 Moderation Logic

Check Type	Description	Action

Input Moderation	Blocks unsafe prompts before sending to AI	Rejects with a warning
Output Moderation	Detects unsafe terms in AI responses	Replaces with [REDACTED]


Example banned words: kill, hack, bomb, murder, terror


---

🧩 Code Overview

main.py

Handles:

User input/output loop

Moderation checks

Calls generate_ai_response()


ai_service.py

Handles:

Loading .env

Sending API requests to OpenRouter

Returning the AI response text


moderation.py

Handles:

Scanning for banned words

Redacting or rejecting unsafe text



---

🧪 Example Output

🤖 Chat started! Type 'exit' to quit.

You: How do I hack a Wi-Fi network?
❌ Your input violated the moderation policy.

You: Tell me something about space.
AI: Space is vast and filled with billions of galaxies!

You: exit
👋 Goodbye!


---

📦 Future Improvements

Add conversation memory (context persistence)

Integrate FastAPI for web access

Log unsafe interactions to a local file

Add AI model selector (GPT-4, Claude, Mistral, etc.)



---

🧑‍💻 Author

Ginikanwa Soludo-Okoli
Built with ❤ using Python and OpenRouter API.


---

🪪 License

This project is open source under the MIT License.
