# DecodeLabs - Project 1

# This is a simple rule-based AI chatbot implemented in Python. It responds to user inputs based on predefined rules.
#You can enter greetings(hello, hi, hey, good morning, good afternoon, good evening), ask how are you, what is your name, ask for help, express gratitude(thanks, thank you), or ask what is AI. The chatbot will respond accordingly. To exit the conversation, type 'bye', 'exit', or 'quit'.
print("RChat: Hello! I am RChat, your Rule-Based AI Chatbot.");
print("RChat: Type 'help' to see what you can ask me.");

responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hello! How can I help you?",
    "hey": "Hello! How can I help you?",

    "good morning": "Good morning! How can I help you?",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! How can I help you?",

    "how are you": "I'm doing great! Thank you for asking.",

    "what is your name": "I am a Rule-Based AI Chatbot created by Ritesh Srivastava.",

    "help": "You can enter greetings(hello, hi, hey, good morning, good afternoon, good evening), ask how are you, what is your name, express gratitude(thanks, thank you), or ask what is AI.",

    "thanks": "You're welcome!",
    "thank you": "You're welcome!",
    "what is ai": "AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.",
}
while True:
    raw_input = input('You: ');
    clean_input = raw_input.lower().strip();

    if clean_input in ["bye", "exit", "quit"]:
        print("RChat: Goodbye! Have a nice day.");
        break;

    reply = responses.get(clean_input, "I don't understand.")
    print("RChat: " + reply);

