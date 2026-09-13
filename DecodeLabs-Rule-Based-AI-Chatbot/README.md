# DecodeLabs Rule-Based AI Chatbot

## Project 1

This project implements a simple rule-based chatbot in Python. It responds to predefined user inputs and keeps the conversation running until the user enters an exit command.

## Requirements Covered

- Continuous input loop
- Input normalization for case and extra whitespace
- More than five predefined intents stored in a dictionary
- Rule-based control flow for exit handling and response selection
- Default fallback response for unknown inputs
- Clean exit using `bye`, `exit`, or `quit`

## Files

```text
DecodeLabs-Rule-Based-AI-Chatbot/
|-- README.md
|-- chatbot.py
`-- tests/
    `-- test_chatbot.py
```

## Run

From this project folder:

```bash
python chatbot.py
```

Example:

```text
DecodeLabs Rule-Based Chatbot
Type 'bye', 'exit', or 'quit' to end the conversation.
You: hello
Bot: Hello. How can I help you?
You: what is your name
Bot: I am the DecodeLabs rule-based chatbot.
You: exit
Bot: Goodbye.
```

## Test

If `pytest` is installed:

```bash
pytest -q
```

The tests cover input normalization, known responses, fallback behavior, and exit handling.
