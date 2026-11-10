"""A small, rule-based command-line chatbot for the CodeAlpha Python task."""


def get_reply(message: str) -> str:
    """Return a predefined response for a supported message."""
    normalized = " ".join(message.casefold().strip().split())

    if normalized in {"hello", "hi", "hey"}:
        return "Hi! How can I help you today?"
    if normalized in {"how are you", "how are you?", "how are you doing"}:
        return "I'm fine, thanks! How are you?"
    if normalized in {"what is your name", "what's your name", "your name"}:
        return "I'm CodeAlpha Bot, a simple rule-based chatbot."
    if normalized in {"help", "what can you do"}:
        return "Try saying hello, asking how I am, asking my name, or typing bye to exit."
    if normalized in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! Have a great day!"
    return "I'm not sure how to respond to that yet. Type 'help' to see what I understand."


def chat() -> None:
    """Run the conversation until the user says goodbye or exits."""
    print("CodeAlpha Bot: Hello! I'm CodeAlpha Bot. Type 'help' for ideas or 'bye' to exit.")

    while True:
        try:
            message = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nCodeAlpha Bot: Goodbye! Have a great day!")
            break

        reply = get_reply(message)
        print(f"CodeAlpha Bot: {reply}")
        if " ".join(message.casefold().strip().split()) in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    chat()
