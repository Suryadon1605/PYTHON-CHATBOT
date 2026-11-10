# CodeAlpha Basic Chatbot

A beginner-friendly, rule-based chatbot that runs in a terminal. It responds to a small set of phrases with predefined messages and continues until the user says `bye` (or another supported exit word).

## Requirements

- Python 3.8 or later
- No third-party packages
- A terminal or command prompt

## Run it

```bash
python chatbot.py
```

On some systems, use `python3 chatbot.py` instead.

## Try these messages

- `hello`, `hi`, or `hey`
- `how are you`
- `what is your name`
- `help`
- `bye` to end the conversation

The bot also responds safely to unrecognized input with a help hint. Matching ignores capitalization and extra spaces.

## Example

```text
CodeAlpha Bot: Hello! I'm CodeAlpha Bot. Type 'help' for ideas or 'bye' to exit.
You: hello
CodeAlpha Bot: Hi! How can I help you today?
You: how are you
CodeAlpha Bot: I'm fine, thanks! How are you?
You: bye
CodeAlpha Bot: Goodbye! Have a great day!
```

## How it works

1. `chat()` prints a welcome message and repeatedly reads input.
2. `get_reply()` normalizes the message and chooses a predefined response with `if`/`elif`-style rules.
3. A goodbye phrase ends the loop. End-of-file and Ctrl+C also exit cleanly.

This project demonstrates functions, strings, conditionals, loops, and console input/output. It does not use machine learning or an online service.

## Project structure

```text
CodeAlpha_Basic_Chatbot/
├── chatbot.py
├── README.md
├── sample_output.txt
├── video_explanation_script.md
├── linkedin_post_draft.md
└── submission_checklist.md
```

## Internship submission reminder

The supplied CodeAlpha task PDF says source code should be uploaded to GitHub in a repository named `CodeAlpha_ProjectName`, a project explanation video should be posted on LinkedIn with the repository link, and the task should be submitted through the form shared in the WhatsApp group. Follow the latest instructions from your program coordinator for eligibility and deadline details.
