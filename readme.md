# RChat - Rule-Based AI Chatbot

A simple Python chatbot that responds to user inputs using predefined rules and keyword matching. This project is designed as a beginner-friendly example of a rule-based conversational agent.

## Features

- Responds to greetings like `hello`, `hi`, and `good morning`
- Answers basic questions such as:
  - `how are you`
  - `what is your name`
  - `what is AI`
  - `help`
- Handles gratitude phrases such as `thanks` and `thank you`
- Allows users to exit the chat using `bye`, `exit`, or `quit`
- Easy to understand and extend with new rules

## Project Overview

This chatbot uses a Python dictionary of predefined responses. It reads user input, converts it to lowercase, trims whitespace, and matches the cleaned input against known phrases. If the phrase is recognized, it prints the corresponding response; otherwise, it returns a fallback message.

## Files

- `Chatbot.py` - Main chatbot logic
- `readme.md` - Project documentation

## How to Run

1. Make sure Python is installed on your system.
2. Open a terminal in the project folder.
3. Run:

```bash
python Chatbot.py
```

## Example Interactions

```text
You: hello
RChat: Hello! How can I help you?

You: how are you
RChat: I'm doing great! Thank you for asking.

You: what is AI
RChat: AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.

You: exit
RChat: Goodbye! Have a nice day.
```

## Sample Supported Inputs

- `hello`
- `hi`
- `hey`
- `good morning`
- `good afternoon`
- `good evening`
- `how are you`
- `what is your name`
- `help`
- `thanks`
- `thank you`
- `what is ai`
- `bye`
- `exit`
- `quit`

## Future Improvements

This project can be extended by adding:

- More conversational patterns
- A larger response dictionary
- Text preprocessing for better matching
- More advanced NLP logic
- GUI-based chatbot interface

## Author

Created by Ritesh Srivastava.

## License

This project is open for educational and personal use.
