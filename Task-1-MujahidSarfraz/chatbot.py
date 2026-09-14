"""Rule-based command-line chatbot for DecodeLabs Project 1."""

RESPONSES = {
    "hello": "Hello. How can I help you?",
    "hi": "Hi. How can I help you?",
    "hey": "Hey. What can I do for you?",
    "how are you": "I am doing well. Thanks for asking.",
    "what is your name": "I am the DecodeLabs rule-based chatbot.",
    "help": "You can greet me, ask my name, ask how I am, or type an exit command.",
    "thanks": "You are welcome.",
    "thank you": "You are welcome.",
}

EXIT_COMMANDS = {"bye", "exit", "quit"}
FALLBACK_RESPONSE = "I do not understand that input. Please try another message."
EXIT_RESPONSE = "Goodbye."


def normalize_input(value: str) -> str:
    """Normalize case and surrounding whitespace before matching."""
    return " ".join(value.strip().lower().split())


def generate_response(user_input: str) -> tuple[str, bool]:
    """Return a response and whether the conversation should stop."""
    cleaned_input = normalize_input(user_input)

    if cleaned_input in EXIT_COMMANDS:
        return EXIT_RESPONSE, True
    else:
        response = RESPONSES.get(cleaned_input)
        if response is None:
            return FALLBACK_RESPONSE, False
        return response, False


def run_chatbot() -> None:
    """Run the chatbot until the user enters an exit command."""
    print("DecodeLabs Rule-Based Chatbot")
    print("Type 'bye', 'exit', or 'quit' to end the conversation.")

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\nBot: {EXIT_RESPONSE}")
            break

        response, should_exit = generate_response(user_input)
        print(f"Bot: {response}")

        if should_exit:
            break


if __name__ == "__main__":
    run_chatbot()
