def chatbot():
    print("================================")
    print("       BASIC CHATBOT")
    print("================================")
    print("Type 'hello', 'how are you', or 'bye'")
    print("Type 'exit' to close the chatbot.")
    print()

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        elif user_input == "exit":
            print("Bot: Chatbot closed.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()