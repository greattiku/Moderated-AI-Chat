

from moderation import contains_banned_words, redact_banned_words
from ai_service import generate_ai_response

def main():
    system_prompt = "You are a polite and helpful assistant. Always respond safely and clearly."
    print(" ")
    print(" 🤖 Chat started! Type 'exit' to quit.\n")

    while True:
        user_prompt = input("You: ")

        if user_prompt.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        if contains_banned_words(user_prompt):
            print("❌ Your input violated the moderation policy.")
            continue

        try:
            ai_response = generate_ai_response(system_prompt, user_prompt)

            if contains_banned_words(ai_response):
                ai_response = redact_banned_words(ai_response)
                print("⚠ Some parts of the AI response were redacted.\n")

            print("AI:", ai_response, "\n")

        except Exception as e:
            print("Error:", e)
            break

if __name__ == "__main__":
    main()