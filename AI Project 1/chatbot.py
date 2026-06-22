# Rule-Based AI Chatbot

print("🤖 AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you today?")

    elif user_input == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user_input == "what is your name":
        print("Bot: My name is RuleBot.")

    elif user_input == "help":
        print("Bot: I can respond to greetings and simple questions.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")